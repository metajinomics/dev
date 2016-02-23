#!/usr/bin/python
# this script calculate how many sequences are found by primer set
#usage: python get_percent_b_merge.py Primer.Party_SeqscoveredUniform cdhit.prot.seqs.inti1.fa.clstr

import sys
import os
from collections import Counter
import re

def read_id (filename):
    dict = {}
    for line in open(filename,'r'):
        dict[line.strip().split('.')[0]]=0
    return dict

def read_map(filename,dict):
    total = 0
    fread = open(filename,'r')
    j = 0
    tempid = ""
    for n,line in enumerate(fread):
        line = line.rstrip()
        if line.startswith(">Cluster"):
            i = n
            string = re.split("\n",line)
            id = string[0]
            if not j == 0:
                #print"contig_count = ",j
                total = total + j
                if dict.has_key(tempid):
                    dict[tempid]=j
                j = 0
                tempid = ""
        elif line.endswith("*"):
            lexeme = re.split("\t| |>|\...",line)
            contig = lexeme[3]
            j = j+1
            #print '%s\t%s\t%s' %(i,id,contig)
            tempid = contig
        else:
            j = j+1
    #print "contig_count=",j
    total = total + j
    if dict.has_key(tempid):
        dict[tempid]=j
    #print total

    return total,dict

def get_num(id1):
    id1dict = read_id(id1)
    mapfile = sys.argv[2]
    maptotal,mapdict = read_map(mapfile,id1dict)
    return maptotal,mapdict

def main():
    #read id
    pair = [1,2,3,5,10]
    for x in pair:
        id1 = sys.argv[1]+str(x)
        id1total,id1dict = get_num(id1)
        total = 0
        numprim = x
        for i in id1dict.items(): 
            total = total + i[1]
        percent = total*100/id1total
        print numprim,'pair',total,'/',id1total,'\t',percent,'%'

if __name__ == '__main__':
    main()
