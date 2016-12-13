#!/usr/bin/python

#this script separate fasta file into multiple files
#
import sys
import utils

fasta = utils.read_fasta(sys.argv[1])
for item in fasta.items():
    name = item[0].split(' ')[0][1:]+'.fa'
    fwrite = open(name,'w')
    fwrite.write("%s\n%s\n" %(item[0], item[1]))
    fwrite.close()
