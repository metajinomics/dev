#!/usr/bin/python

# this script validate primer by using output file of blast
#usage : python validata_primer_using_blast.py blast.out
import sys

def main():
    print "here"
    #read blast file put into dictionary
    #key will be hit, contents will be primers
    d = {}

    for line in open(sys.argv[1],'r'):
        spl = line.strip().split('\t')

        if d.has_key(spl[1]):
            d[spl[1]].append(spl[0])
        else:
            d[spl[1]] = [spl[0]]
    for item in d.items():
        print '%s %s' %(item[0],','.join(item[1]))

   #print or analyze

    #genome F-R primer both found

    #shared primer??

if __name__ == '__main__':
    main()
