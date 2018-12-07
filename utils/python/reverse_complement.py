#!/usr/bin/python
from string import maketrans

def get_rc(seq):
    seq = seq.upper()
    trans = maketrans("AGCT","TCGA")
    if isinstance(seq, unicode):
        seq = seq.encode("ascii")
    seq = seq.translate(trans)
    seq = seq[::-1]
    return seq

def get_from_url(seq):
    spl = seq.split('\n')
    if(len(spl)>1):
        spl[1]= get_rc(spl[1])
    seq = '\n'.join(spl)
    return seq
