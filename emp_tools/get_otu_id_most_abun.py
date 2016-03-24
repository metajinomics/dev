#!/usr/bin/pyhon
import sys

dict={}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split(' ')
    dict[spl[0]]=spl[1]
flag = 0
for line in open(sys.argv[2],'r'):
    if flag==0:
        if(line[:21]=="Counts/sample detail:"):
            flag = 1
    else:
        spl = line.strip().split(':')
        if len(spl)>1:
            if(dict.has_key(spl[1].strip())):
                print line.strip()
