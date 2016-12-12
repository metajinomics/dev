#!/usr/bin/python

#this script make flag on primers
#usage: python put_flag_primers.py pcr.prediction.out 

import sys

def put_flag(d, primer,flag):
    if d.has_key(primer):
        if flag == 1:
            d[primer]["good"] = d[primer].get("good",0)+1
        else:
            d[primer]["bad"] = d[primer].get("bad",0)+1
    else:
        d[primer] = {}
        if flag == 1:
            d[primer]["good"] = 1
        else:
            d[primer]["bad"] = 1

def main():
    d = {}
    for line in open(sys.argv[1],'r'):
        spl =  line.strip().split(' ')
        length = int(spl[5])
        fpri = spl[1]
        rpri = spl[3]
        flag = 0
        if length > 200 and length < 300:
            flag = 1
            put_flag(d,fpri,flag)
            put_flag(d,rpri,flag)
        else:
            flag = 0
            put_flag(d,fpri,flag)
            put_flag(d,rpri,flag)

    for item in d.items():
        print item[0],item[1]

if __name__ == "__main__":
    main()
