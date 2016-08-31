#show length stat for fasta

#python show_length_stat_fasta.py

import sys
import numpy

def get_length(seqs):
    seq = ''.join(seqs)
    length = len(seq)
    return length

def main():
    flag = 0
    seqs = []
    alen = []
    for line in open(sys.argv[1],'r'):
        if(line[:1] == ">" and flag == 0):
            #name = line.strip()
            flag = 1
        elif(line[:1] == ">" and flag == 1):
            length = get_length(seqs)
            alen.append(length)
            #name = line.strip()
            seqs = []
        else:
            seqs.append(line.strip())
    length = get_length(seqs)
    alen.append(length)
    print "Average length: "+str(numpy.mean(alen))
    print "Minimum length: "+str(numpy.amin(alen))
    print "Maximum length: "+str(numpy.amax(alen))
if __name__ == '__main__':
    main()
