#!/usr/bin/python
# python make_abun_table.py soil_type_count.txt refsoil_emp_blast.out.txt

import sys

dict = {}
for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    dict[spl[0]]=line.strip()

for line in open(sys.argv[2],'r'):
    spl = line.strip().split('\t')
    if (dict.has_key(spl[1])):
        temp = [spl[0],dict[spl[1]]]
        print '\t'.join(temp)
