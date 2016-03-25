#!/usr/bin/python
# usage: python get_count_from_blast.py refsoil_emp_blast.out.txt /mnt/data2/jin_emp/emp/soil_emp_table.summary
import sys
dict={}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    dict[spl[1]]=0

#print len(dict)
#print dict
add = 0
flag = 0
for line in open(sys.argv[2],'r'):
    if(flag==0):
        if(line[:21]=="Counts/sample detail:"):
            flag=1
    else:
        spl = line.strip().split(':')
        if(dict.has_key(spl[0])):
           add = add + int(spl[1].strip().split('.')[0])

print add
