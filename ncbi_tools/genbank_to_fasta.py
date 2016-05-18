#!/usr/bin/python
#This script find protein sequence and nucleotide sequence from given gene information
#usage: python gene_list_to_seq.py listgenome folder protein_seq.fa nucleo_seq.fa
#input file: NCBI_accession_number 
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
def read_genbank(item,dir):
    genbankname = dir+"/"+item+".gbk"
    genome=SeqIO.read(genbankname, 'genbank')
    dat= SeqIO.parse(genbankname, 'genbank')
    return genome,dat

def write_protein(feat,record,output_handle,name):
    if not ('translation' in feat.qualifiers):
        return 
    output_handle.write(">%s from %s\n%s\n" % (name,record.name,feat.qualifiers['translation'][0]))

def write_nu(feat,record,genome,nu_out,name):
    nu_out.write(">%s from %s\n%s\n" % (name,record.name,feat.extract(genome.seq)))

#check if the gene is presence in the genbank file
def check_gene(genome,record,output_handle,nu_out):
        for feat in genome.features:
            if feat.type == "CDS":
                r= feat.location
                name = "unkown"
                if ("locus_tag" in feat.qualifiers):
                    name = feat.qualifiers['locus_tag'][0]
                elif ("gene" in feat.qualifiers):
                    name =feat.qualifiers['gene'][0]
                write_protein(feat,record,output_handle,name)
                write_nu(feat,record,genome,nu_out,name)

        
def main():
    #read id file
    fread = open(sys.argv[1],'r')
    dir = sys.argv[2]
    output_handle = open(sys.argv[3], "w")
    nu_out = open(sys.argv[4],'w')
    for line in fread:
        spl = line.strip().split('\t')
        ids = spl[0]
        #read genbank file
        genome,dat = read_genbank(ids,dir)
        #run
        for record in list(dat):
            check_gene(genome,record,output_handle,nu_out)

        
if __name__ == '__main__':
    main()


