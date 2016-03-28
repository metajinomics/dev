#!/usr/bin/pyhon
#usage: python get_otu_abun.py list.otu.txt summaryfile
import sys

dict={}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    dict[spl[0]]=0
flag = 0
add = 0
for line in open(sys.argv[2],'r'):
    if flag==0:
        if(line[:21]=="Counts/sample detail:"):
            flag = 1
    else:
        spl = line.strip().split(':')
        if len(spl)>1:
            if(dict.has_key(spl[0].strip())):
                add = add + int(spl[1].strip().split('.')[0])
print add
