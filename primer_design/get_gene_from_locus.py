
#python get_gene_from_locus.py list_locus.txt usda.nu.fna > reca.nu.fa

import sys

dict = {}
for line in open(sys.argv[1],'r'):
    #spl = line.strip().split(': ')[1]
    #dict[spl]=spl
    dict[line.strip()] = line.strip()

flag = 0
for line in open(sys.argv[2],'r'):
    if(line[:1] == ">"):
        ids = line.split(' ')[0][1:]
        if(dict.has_key(ids)):
            print line.strip()
            flag = 1
    elif(line[:1] != ">" and flag == 1):
        print line.strip()
        flag = 0
    else:
        continue
