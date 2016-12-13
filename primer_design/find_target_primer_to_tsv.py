#!/usr/bin/python

#usage: python find_target_primer_to_tsv.py pcr.product.txt > one.tsv
# cat *.pcr.product.txt > argname.txt
# for x in *.pcr.product.txt;do python find_target_primer_to_tsv.py $x;done > one.tsv

import sys
min = 180
max = 280
i = 0
name = ""
file = sys.argv[1]
for line in open(file,'r'):
    spl = line.strip().split(' ')
    if line[:1] == ">" and name != spl[0][1:]:
        length = int(spl[len(spl)-1])
        if length > min and length < max:
            name = spl[0][1:]
            fpri = spl[len(spl)-5].split("(")[0]
            rpri = spl[len(spl)-3].split("(")[0]
            i += 1
            print "%s\t%s\t%s\t%s\t%s" %(file.split('.')[0],name,fpri,rpri,length)
    elif name == spl[0][1:]:
        continue
