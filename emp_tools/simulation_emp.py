#!/usr/bin/python
# 
#usage: python similation_emp.py summary > output
import sys

fread = open(sys.argv[1],'r').readlines()
i = 0
sum = 0
flag = 0
for line in reversed(fread):
    if flag == 1:
        continue
    if(line[:21] == "Counts/sample detail:"):
        flag = 1
        continue
    spl = line.strip().split(':')
    sum = sum + float(spl[1].strip())
    print '\t'.join([str(i),str(sum)])
