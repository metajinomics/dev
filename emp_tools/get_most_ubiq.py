#!/usr/bin/python
#usage: python get_most_ubiq.py 100most_uniq.txt soil_emp_table.nonzero ../soil_emp_table.biom ../Soil_EMP_taxonomy/JavaNewSoilRepSet_tax_assignments.txt
import sys

dict = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split(' ')
    dict[spl[0]]=spl[1]
i = 0
dict2 = {}
for line in open(sys.argv[2],'r'):
    if(dict.has_key(line.strip())):
       dict2[i]=line.strip()
    i += 1

#print len(dict2)
#print dict2

from biom import load_table
from biom.table import Table
import numpy as np
dict3={}
table = load_table(sys.argv[3])
b = table.ids(axis='observation')
for x in dict2.items():
    dict3[b[x[0]]]=x[1]

for line in open(sys.argv[4]):
    spl = line.strip().split('\t')
    if(dict3.has_key(spl[0])):
        out = [dict3[spl[0]],line.strip()]
        print '\t'.join(out)

