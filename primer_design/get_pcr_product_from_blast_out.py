#!/usr/bin/python

# this script find pcr product from blast output
# usage: python get_pcr_product_from_blast_out.py blastout > output

import sys

def find_product(target, hits):
    f = {}
    r = {}
    for x in hits:
        spl = x.split('\t')
        dir = ""
        if int(spl[8]) < int(spl[9]):
            dir = "F"
            f[spl[0]] = int(spl[8])
        else:
            dir = "R"
            r[spl[0]] = int(spl[8])
        #print target, spl[0], spl[8], spl[9], dir
    #print f,r
    for fitem in f.items():
        for ritem in r.items():
            length = ritem[1] - fitem[1]
            if length > 0:
                print target, fitem[0], fitem[1],ritem[0],ritem[1],length
    return 0

def main():
    blast = sys.argv[1]
    d = {}
    for line in open(blast,'r'):
        spl = line.strip().split('\t')
        #id = spl[1].split('|')[3]
        id = spl[1]
        if d.has_key(id):
            d[id].append(line.strip())
        else:
            d[id] = [line.strip()]
    for item in d.items():
        find_product(item[0],item[1])

if __name__ == "__main__":
    main()
