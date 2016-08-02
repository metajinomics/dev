#
#get gene from list
#python get_gene_from_list.py list_gene.txt full.fasta > listed_gene.fa

import sys
dict = {}
for line in open(sys.argv[1],'r'):
    dict[line.strip()]=line.strip()

flag = 0
for line in open(sys.argv[2],'r'):
    if(line[:1]==">"):
        sp = line.split(' ')
        spl=sp[0].split('|')
        #print spl[len(spl)-1]
        if(dict.has_key(spl[len(spl)-1])):
            print line,
            flag = 1
    elif(line[:1]!=">" and flag == 1):
        print line,
        flag = 0
    else:
        continue
