#!/usr/bin/python
#usage: python soil_type_refsoil.py refsoil_emp_blast.out.txt soil_type_norm.unix.txt RefSoil_v1.txt 
import sys
blast_read = open(sys.argv[1], 'r')
blast_dict = {}
for line in blast_read:
   spl = line.strip().split('\t')
   blast_dict[spl[0]] = spl[1]
blast_read.close()

soil_read = open(sys.argv[2],'r')
soil_dict = {}
soil_header = soil_read.next()
for line in soil_read:
    spl = line.strip().split('\t')
    temp = []
    for i in range(1,10):
        temp.append(spl[i])
    soil_dict[spl[0]]= temp
soil_read.close()

ref_read = open(sys.argv[3],'r')
line = ref_read.next()
tempp = [line.strip(),soil_header.strip()]
print '\t'.join(tempp)
for line in ref_read:
    spl = line.strip().split('\t')
    if (blast_dict.has_key(spl[0])):
        temp_emp_id = blast_dict[spl[0]]
        soil_type = soil_dict[temp_emp_id]
        soil_info = '\t'.join(soil_type)
        temp = [line.strip(),temp_emp_id,soil_info]
        print '\t'.join(temp)
    else:
        print line.strip()
    
