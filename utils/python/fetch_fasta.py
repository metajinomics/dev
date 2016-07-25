import urllib2
import os
import sys
import time
import reverse_complement

def from_blast(filename):
    for line in open(filename,'r'):
        spl = line.strip().split('\t')
        id = spl[1].split('|')[1]
        seq = get_fasta(id,spl[8],spl[9])
        print seq,

def get_fasta(id,start,end):
    url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={0}&seq_start={1}&seq_stop={2}&rettype=fasta&retmode=text"
    s1 = url_template.format(id,start,end)
    seq = urllib2.urlopen(s1).read()
    return seq

def from_multi_blast(filename):
    ids = ""
    flag = 0
    seqs = []
    gen = 1
    fwrite = open('map_file.txt','w')
    for line in open(filename,'r'):
        spl = line.strip().split('\t')
        id = spl[1].split('|')[1]
        if (spl[0] == ids):
            seq = get_fasta(id,spl[8],spl[9])
            seqs.append(seq)
        elif (flag == 0 and spl[0] != ids):
            gname = 'gene' + str(gen)
            gen += 1
            fwrite.write(gname+'\t'+ spl[0]+'\n')
            gbk_out_file = os.path.join('./',gname+'.fa')
            flag = 1
            ids = spl[0]
        elif (flag == 1 and spl[0] != ids):
            gname = 'gene' + str(gen)
            gen+= 1
            fwrite.write(gname+'\t'+spl[0]+'\n')
            open(gbk_out_file, "w").write(''.join(seqs))
            gbk_out_file = os.path.join('./',gname+'.fa')
            ids = spl[0]
    open(gbk_out_file, "w").write(''.join(seqs))
