import argparse
import numpy as np
from decimal import Decimal



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--table', help='input table file')
    parser.add_argument('-m', '--max_value', default=1, help='the max value in the dist matrix')
    parser.add_argument('-o', '--out', help='output table file')
    args = parser.parse_args()

    fn_table  = args.table
    max_value = args.max_value
    fn_out    = args.out

    fn = open(fn_table, 'r')
    fo = open(fn_out, 'w')
    for line in fn:
        fields = line.split()
        if len(fields) > 1:
            fo.write(fields[0])
            for ele in fields[1:-1]:
                number = Decimal(max_value) - Decimal(float(ele))
                fo.write('\t' + str(number))
            fo.write('\n')
        else:
            fo.write(line)
    fo.close()
    fn.close()
