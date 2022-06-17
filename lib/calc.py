import os
import sys
import logging
import pandas
import itertools
import re
import multiprocessing
import signal

__author__ = 'jmrodriguezc'

signal.signal(signal.SIGINT, signal.SIG_IGN)

class calculate:
    '''
    Extract the correlation values
    '''
    NUM_CPUs = int(multiprocessing.cpu_count()/1.25) # use the 75% of whole cpus
    # NUM_CPUs = 20

    def __init__(self, i, m=None, uniq_geneId=False, transpose=False, groups=None):
        # handle I/O files
        self.infile = i
        # extract input data ( as dataframe )
        # set index with the first column
        fname, fextension = os.path.splitext(self.infile)
        if fextension == ".xlsx" or fextension == ".xls":
            self.df = pandas.read_excel(self.infile, na_values=['NA'])
        elif fextension == ".csv":
            self.df = pandas.read_csv(self.infile, sep=",", na_values=['NA'], encoding="ISO-8859-1")
        elif fextension == ".tsv" or fextension == ".txt":
            self.df = pandas.read_csv(self.infile, sep="\t", na_values=['NA'], encoding="ISO-8859-1")
        else:
            sys.exit("ERROR: extension of input file is not correct")
        c = str(self.df.columns[0])
        self.df = self.df.set_index(c)
        # convert to float64
        self.df.astype('float64').dtypes
        # transpose if apply
        if transpose:
            self.df = self.df.transpose()
        # get method
        if m is None:
            self.method = 'pearson'
        else:
            self.method = m
        # return or not the Unique Gene Id
        self.uniqGeneId = uniq_geneId
        # group the list of combinations or not
        self.groups = groups
        # ouput config
        self.out_header = ['Qi','Qj','Rij','Nij']
        self.df_corr = pandas.DataFrame()
        
    def _get_id(self, desc):
        '''
        Extract the id from the description
        '''
        if self.uniqGeneId:
            if desc.startswith(">"):
                gid = 'UNKNOWN'
                if re.search(r'GN=(\w*)', desc, re.I | re.M):        
                    g_id = re.search(r'GN=(\w*)', desc, re.I | re.M)
                    gid = str(g_id[1])
                # the protein_id is mandatory
                p_id = desc.split("|")
                if p_id is not None and len(p_id) >= 2:
                    pid = str(p_id[1])
                    id = gid +"|"+ pid
                else:
                    id = desc
            else:
                id = desc
        else:
            id = desc
        return id

    def _append_correlation(self, shared_lst, combos):
        for combo in combos:        
            # get index
            qi = combo[0]
            qj = combo[1]
            # create the correlation
            dfi = self.df.loc[qi,:]
            dfj = self.df.loc[qj,:]
            corr = dfi.corr(dfj, method=self.method)
            # count hte number of cases when both series are empty
            # joining the df and deleting when all columns are empty
            n = pandas.concat([dfi, dfj], axis=1)
            n = n.dropna(how='all')
            nij = len( n.index )
            # extract the identifiers by protein gene|protein
            gi = self._get_id(qi)
            gj = self._get_id(qj)
            # append the list of values into shared list
            shared_lst.append([gi,gj,corr,nij])

    def correlation(self, method=None):
        '''
        Calculate the correlation
        '''
        # get method if it exists: Priority
        if method is not None:
            self.method = method
        # from 'tag' of groups, we create a list of groups and compute the cartesian product
        combos = []
        if self.groups:
            idx = self.df.index.tolist()
            groups = []
            for group in self.groups.split(","):
                g = [x for x in idx if x.find(group) != -1]
                groups.append(g)
            combos = list(itertools.product(*groups))
        # from the list of proteins (index) we get all combinatios for pairs appending into the queue
        else:
            idx = self.df.index.tolist()
            combos = list( itertools.combinations(idx, 2) )
        combos_len = len( combos )
        logging.info("number of combinations "+str(combos_len)+" from "+str(len(idx))+" items")
        # Shared list (Proxy manager)
        mgr = multiprocessing.Manager()
        shared_lst = mgr.list()
        # create multiprocessing Pool
        logging.info("calculate the correlation in parallel: "+str(self.NUM_CPUs))
        pool = multiprocessing.Pool(processes=self.NUM_CPUs)
        # split the list of combinations to go through to each CPUs
        for cmbs in [combos[i:i+self.NUM_CPUs] for i  in range(0, combos_len, self.NUM_CPUs)]:
            pool.apply_async(self._append_correlation, args=(shared_lst, cmbs, ))
        # close and block until all tasks are done
        pool.close()
        pool.join()
        # convert multiprocessing.managers.ListProxy to list
        shared_lst = list(shared_lst)
        # create dataframe with the list of lists
        self.df_corr = pandas.DataFrame(shared_lst, columns=self.out_header)


    def to_csv(self, outfile):
        '''
        Print to CSV sorting by score
        '''
        # sort dataframe by correlation score (Third column)
        if not self.df_corr.empty:
            c = str(self.df_corr.columns[2])        
            self.df_corr = self.df_corr.sort_values(by=[c], ascending=False)
            self.df_corr.to_csv(outfile, index=False)
        else:
            logging.error("Empty output")
