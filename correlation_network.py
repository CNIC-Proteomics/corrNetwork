#!/usr/bin/python

import os
import sys
import argparse
import logging

# import local modules
sys.path.append( os.path.abspath(os.path.dirname(__file__)) )
# import calc # for unlocated virtual environment
from lib import calc # for local environment

__author__ = 'jmrodriguezc'

def main(args):
    ''' Main function'''

    logging.info('create calculator object')
    w = calc.calculate(args.infile, args.method, args.uniq_geneId, args.transpose, args.groups)

    logging.info('calculate the correlation: '+args.method)
    w.correlation()

    logging.info('print the correlation file')
    w.to_csv(args.outfile)


if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser(
        description='Gets the correlation values for the proteins in multiple patients.',
        epilog='''
        Example:
            correlation_network.py -i test/PESA_V1.xlsx -o test/PESA_V1.corr_net.pearson.csv
        ''')
    parser.add_argument('-i',   '--infile', required=True, help='Excel file with the Zq for proteins/patients')
    parser.add_argument('-o',   '--outfile', required=True, help='Output file with the correlation values in CSV format')
    parser.add_argument('-m',   '--method', default='pearson', choices=['pearson', 'kendall', 'spearman'], help='Excel file with the Zq for proteins/patients')
    parser.add_argument('-g',   '--uniq_geneId', action='store_true', help="Get gene unique id")
    parser.add_argument('-t',   '--transpose', action='store_true', help="Transpose the input table")
    parser.add_argument('-gr',  '--groups', help="List of 'tags' that belong to identify the group of combinations")
    parser.add_argument('-v', dest='verbose', action='store_true', help="Increase output verbosity")
    args = parser.parse_args()

    # logging debug level. By default, info level
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info('start '+os.path.basename(__file__))
    main(args)
    logging.info('end '+os.path.basename(__file__))