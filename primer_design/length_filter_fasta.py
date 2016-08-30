#this script filter short sequence
#usage: python length_filter_fasta.py fastafile length > outputfile
#python length_filter_fasta.py fasta.fa 300 > fasta_over300.fa

import sys
def check_length(name,seqs,cu):
    seq = ''.join(seqs)
    if(len(seq) >= cu):
        print name
        print seq

def main():
    fread = open(sys.argv[1],'r')
    cu = int(sys.argv[2])
    name = ''
    seqs = []
    flag = 0
    for line in fread:
        if(line.strip()[:1] == ">" and flag == 0):
            name = line.strip()
            flag = 1
        elif(line.strip()[:1] == ">" and flag == 1):
            check_length(name,seqs,cu)
            name = line.strip()
            seqs = []
        else:
            seqs.append(line.strip())
    check_length(name,seqs,cu)

if __name__ == '__main__':
    main()
