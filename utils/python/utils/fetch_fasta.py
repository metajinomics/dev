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
