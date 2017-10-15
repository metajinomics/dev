#!/usr/bin/python

"""
this script make table from besthit
usage: python make_table.py db.fasta *.besthit
"""

import sys

def main():
    db_file = sys.argv[1]
    besthit_files = sys.argv[2:]
    gene_name = {}
    for line in open(db_file,'r'):
        if line[:1] == ">":
            spl = line[1:].strip().split('|')
            gene_name[spl[1]] = {}

    #now all samples
    all_files = ["-"]
    for each_file in besthit_files:
        spl_name = each_file.strip().split('/')
        file_name = spl_name[len(spl_name)-1]
        all_files.append(file_name)
        for line in open(each_file,'r'):
            spl = line.strip().split('\t')
            name = spl[1].split('|')[1]
            if gene_name[name].has_key(file_name):
                gene_name[name][file_name] += 1
            else:
                gene_name[name][file_name] = 1
    
    #print result
    print '\t'.join(all_files)
    for item in gene_name.items():
        result = []
        for n,file in enumerate(all_files):
            if n == 0:
                result.append(item[0])
                continue
            if item[1].has_key(file):
                result.append(str(item[1][file]))
            else:
                result.append("0")
        print '\t'.join(result)
            

if __name__ == '__main__':
    main()
