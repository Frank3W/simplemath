import codecs
import pkg_resources

import pandas as pd

from simplemath.numbers import EXP

def main():
    print(f'Natural Exp Number: {EXP}')

    # " Note that if a module name is used, then the resource name
    # is relative to the package immediately containing the named module."
    # Here, __name__ is simplemath.print_numbers
    rs = pkg_resources.resource_stream(__name__, 'data/seq.csv')
    utf8_reader = codecs.getreader('utf-8')
    seq_pd = pd.read_csv(utf8_reader(rs))
    print(seq_pd)