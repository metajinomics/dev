#!/usr/bin/python
#This script find protein sequence and nucleotide sequence from given gene information
#usage: python gene_list_to_seq.py ChiA.list.down.txt folder_name protein_seq.fa nucleo_seq.fa
#input file: NCBI_accession_number (tap) gene start position (tap) gene end position (tap) direction
#genbank files are required to store in folder

import os
import json
import urllib
import sys
import subprocess
from Bio import SeqIO
import pycurl
import cStringIO
from Bio.SeqRecord import SeqRecord

#This function read genbank file
def read_genbank(item):
    genbankname = "chia/"+item+".gbk"
    genome=SeqIO.read(genbankname, 'genbank')
    dat= SeqIO.parse(genbankname, 'genbank')
    return genome,dat

def get_genbank(item):#function not used
    id = str(item)
    buf = cStringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://eutils.ncbi.nlm.nih.gov/entrez/\
eutils/efetch.fcgi?db=nuccore&id=' + id + '&rettype=gbwithparts&retmode=text')
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()
    x= buf.getvalue()
    dat = x.split('\n')
    return dat

def check_gene_old(dat,start,end):#function not used
    for n, each in enumerate(dat):
        each = each.strip()
        if each.startswith("CDS"):
            if start in each:
                print n, each

def write_protein(feat,record,output_handle):
    assert len(feat.qualifiers['translation'])==1
    output_handle.write(">%s from %s\n%s\n" % (feat.qualifiers['locus_tag'][0],record.name,feat.qualifiers['translation'][0]))

def write_nu(feat,record,genome,nu_out):
    nu_out.write(">%s from %s\n%s\n" % (feat.qualifiers['locus_tag'][0],record.name,feat.extract(genome.seq)))

#check if the gene is presence in the genbank file
def check_gene(genome,record,start,end,output_handle,nu_out):
        for feat in genome.features:
            if feat.type == "CDS":
                r= feat.location

                if (start in str(r.start) or end in str(r.end)):
                    print feat.location
                    print start, end
                    write_protein(feat,record,output_handle)
                    write_nu(feat,record,genome,nu_out)
                    break

#check if it is bacteria. only bacteria gene will be fetched
def check_bac(genome,dat,start,end,output_handle,nu_out):
    for record in list(dat):
        if "Bacteria" in  record.annotations['taxonomy']:
            check_gene(genome,record,start,end,output_handle,nu_out)
            break
        else:
            print "this is not a bacteria"
            break

def main():
    #read id file
    fread = open(sys.argv[1],'r')
    output_handle = open(sys.argv[2], "w")
    nu_out = open(sys.argv[3],'w')
    for line in fread:
        spl = line.strip().split('\t')
        ids = spl[0]
        start = spl[1]
        end = spl[2]
        dir = spl[3]
        print ids,start,end,dir
        #read genbank file
        genome,dat = read_genbank(ids)
        #run
        check_bac(genome,dat,start,end,output_handle,nu_out)
        
if __name__ == '__main__':
    main()


