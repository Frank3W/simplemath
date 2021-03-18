import codecs
import pkg_resources

import pandas as pd

from simplemath.numbers import EXP

def main():
    print(f'Natural Exp Number: {EXP}')
    rs = pkg_resources.resource_stream('simplemath', 'data/seq.csv')
    utf8_reader = codecs.getreader('utf-8')
    seq_pd = pd.read_csv(utf8_reader(rs))
    print(seq_pd)