import unittest
import os, sys

from pprint import pprint

# import components
from lib import calc

class corrNetworkTests(unittest.TestCase):
    '''
    Battery tests
    '''
    def setUp(self):
        self.indir = os.path.dirname( __file__ ) +'/tests'
        self.infile = self.indir +'/test1-in.xlsx'        
        self.widget = calc.calculate(self.infile)

    def testCorrelationPearson(self):
        method = 'pearson'
        self.widget.correlation(method)
        outfile = self.indir +'/test1-out_'+method+'.csv'
        self.widget.to_csv(outfile)        

    def testCorrelationKendall(self):
        method = 'kendall'
        self.widget.correlation(method)
        outfile = self.indir +'/test1-out_'+method+'.csv'
        self.widget.to_csv(outfile)

    def testCorrelationSpearman(self):
        method = 'spearman'
        self.widget.correlation(method)
        outfile = self.indir +'/test1-out_'+method+'.csv'
        self.widget.to_csv(outfile)

def main():
    unittest.main()

if __name__ == '__main__':
    main()