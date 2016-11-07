#!/usr/bin/python
#this script find left and right length from this hit
#usage: python LRlenght.py blastoutput origianlfile > output

import sys

def print_res(seqs, query, dict):
    fseq = ''.join(seqs)
    left = dict[query][0]
    right = dict[query][1]
    result = [query,str(left),str(len(fseq) - right),str(len(fseq))]
    print '\t'.join(result)

def check_presence(query, dict):
    flag = 0
    if dict.has_key(query):
        flag = 1
    return flag

dict = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    dict[spl[0]] = [int(spl[6]),int(spl[7])]

flag = 0
seqs = []
query = ""
for line in open(sys.argv[2],'r'):
    if line[:1] == ">" and flag == 0:
        query = line.strip()[1:]
        flag = check_presence(query, dict)
    elif line[:1] == ">" and flag == 1:
        print_res(seqs, query, dict)
        seqs = []
        query = line.strip()[1:]
        flag = check_presence(query,dict)
    else:
        if flag == 1:
            seqs.append(line.strip())

if flag == 1:
    print_res(seqs, query, dict)
            
