import logging
import pandas
import itertools
import re

__author__ = 'jmrodriguezc'


class calculate:
    '''
    Extract the correlation values
    '''
    def __init__(self, i, m=None):
        self.infile = i
        self.df = pandas.read_excel(self.infile, na_values=['NA']).set_index('Protein')
        # self.df = self.df.drop( ['Accession'], axis=1) # delete unnecessary columns
        # self.df_full_count = self.df.apply(lambda x: x.count(), axis=1)
        if m is None:
            self.method = 'pearson'
        else:
            self.method = m
        self.out_header = ['Qi','Qj','Rij','Nij']
        self.df_corr = pandas.DataFrame()

    def _get_id(self, desc):
        '''
        Extract the id from the description
        '''
        if desc.startswith("RF_"):
            return desc
        else:
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
            return id

    def correlation(self, method=None):
        '''
        Calculate the correlation
        '''
        # get method if it exists: Priority
        if method is not None:
            self.method = method
        # from the list of proteins (index) we get all combinatios for pairs
        # create a dataframe with the correlation for each pairwise
        idx = self.df.index.tolist()
        for combo in itertools.combinations(idx, 2):
            # get the index name
            qi = combo[0]
            qj = combo[1]
            # create the correlation
            dfi = self.df.loc[qi,:]
            dfj = self.df.loc[qj,:]
            corr = dfi.corr(dfj, method=self.method)
            # count hte number of cases when both series are empty
            # joining the df and deleting when all columns are empty
            n = pandas.concat( [dfi, dfj], axis=1)
            n = n.dropna( how='all')
            nij = len( n.index )
            # extract the identifiers by protein gene|protein
            gi = self._get_id(qi)
            gj = self._get_id(qj)
            # create dataframe with the pairwise
            p = pandas.DataFrame([[gi,gj,corr,nij]], columns=self.out_header)
            # append to global dataframe
            self.df_corr = self.df_corr.append(p, ignore_index=True)
        
    def to_csv(self,outfile):
        '''
        Print to CSV
        '''
        if self.df_corr is not None:
            self.df_corr.to_csv(outfile, index=False)



