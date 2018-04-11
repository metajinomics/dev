#!/usr/bin/python
#usage : python get_definition_from_blast_result.py /Users/jinchoi/Downloads/napA_protein_95_clustered.fa.blastp > description_added.txt

import urllib2
import os
import sys
import time



url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=%s&rettype=gbwithparts&retmode=text"



for id_line in open(sys.argv[1]):
    id = id_line.strip().split('\t')[1]
    if id == "":
        continue

    re = urllib2.urlopen(url_template % id).read()
    spl = re.split('\n')
    for line in spl:
        if "DEFINITION" in line:
            print id_line+'\t'+line.strip().split('  ')[1]

    time.sleep(1.0/3)
