#find which is not present 
#python list_presence.py list file
#python list_presence.py all_args.txt nucleotide_fasta_protein_homolog_model.fasta

import sys
dict = {}
for line in open(sys.argv[1],'r'):
    dict[line.strip()] = 0

for line in open(sys.argv[2],'r'):
    for x in dict.items():
        if(x[0] in line):
            dict[x[0]] += 1

for x in dict.items():
    if(x[1] == 0 ):
        print x[0]
