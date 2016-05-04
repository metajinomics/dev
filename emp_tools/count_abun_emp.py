#!/usr/bin/python
# find abudance 
# usage: python count_abun_emp.py summary id > abun
import sys
sread = open(sys.argv[1],'r')
sum = {}
flag = 0
for line in sread:
    if flag == 0:
        if (line[:21] == "Counts/sample detail:"):
            flag = 1
        continue
    spl = line.strip().split(':')
    sum[spl[0].strip()]=spl[1].strip()
sread.close()

add = 0
for line in open(sys.argv[2],'r'):
    if sum.has_key(line.strip()):
        add = add + float(sum[line.strip()])
print add
