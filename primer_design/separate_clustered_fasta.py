#!/usr/bin/python

#this script separate fasta into cluster
#usage: python separate_clustered_fasta.py original.fasta cluster
import sys
import utils

#read fasta
fasta = utils.read_fasta(sys.argv[1])

#read cluster
cluster = {}
clu_id = {}
clu = ""
for line in open(sys.argv[2],'r'):
    if(line[:1] == ">"):
        clu = line.strip()[1:]
        cluster[clu] = []
    else:
        id = line.strip().split('>')[1].split('...')[0]
        cluster[clu].append(id)
        star  = line.strip().split('>')[1].split('... ')[1]
        if star == "*":
            name = ""
            for x in fasta.items():
                if id in x[0]:
                    name = x[0]
            clu_id[clu] = name.split(' ')[0][1:]

for item in cluster.items():
    file = clu_id[item[0]]+'.clustered.fa'
    fwrite =  open(file,'w')
    for x in fasta.items():
        for y in item[1]:
            if y in x[0]:
                fwrite.write("%s\n%s\n" %(x[0],x[1]))
    fwrite.close()
