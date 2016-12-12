#!/usr/bin/python

#
# python validate_tp_fp.py evaluate tp fp

import sys

def main():
    eval = sys.argv[1]
    tp = open(sys.argv[2],'w')
    fp = open(sys.argv[3],'w')
    for line in open(eval,'r'):
        spl = line.strip().split(' ')
        length = int(spl[5])
        if length >200 and length <300:
            tp.write(line)
        else:
            fp.write(line)

if __name__ == "__main__":
    main()
