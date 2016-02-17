#!/usr/bin/python
import sys


fread = open(sys.argv[1],'r')
locus = ""
for gbline in fread:
    if ("LOCUS" in gbline):
        locus = gbline.strip().split(" ")[7]
    if("organism=" in gbline):
        organism = gbline.strip().split("=")[1][1:-1]
    if(gbline.strip()[:2] == "//" ):
        print locus+"\t"+organism
        locus = ""
        organism = ""
