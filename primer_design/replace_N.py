#python replace_N.py input > output

#this script replace N into - for fasta file

import sys

for line in open(sys.argv[1],'r'):
    if (line[:1] == ">"):
        print line.strip()
    else:
        newline = line.strip().replace("N", "-")
        newline = newline.replace('n','-')
        print newline
