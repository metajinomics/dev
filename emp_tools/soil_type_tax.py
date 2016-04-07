#!/usr/bin/python
import sys
blast_read = open(sys.argv[1], 'r')
blast_dict = {}
for line in blast_read:
   spl = line.strip().split('\t')
   blast_dict[spl[1]] = spl[0]

tax_read = open(sys.argv[2], 'r')
tax_dict = {}
line = tax_read.next()

for line in tax_read:
   
   spl = line.strip().split('\t')
   
   temp = []
   for i in range (6,13):
       temp.append(spl[i])
   tax_dict[spl[0]] = temp

soil_read = open(sys.argv[3], 'r')
line = soil_read.next()
print line
for line in soil_read:
   spl = line.strip().split('\t')
   temp_RefID = blast_dict[spl[0]]
   tax = tax_dict[temp_RefID]
   tax_info = '\t'.join(tax)
   temp = [line.strip(),tax_info]
   print '\t'.join(temp)
