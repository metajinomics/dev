#!/usr/bin/python
#usage: python nonzero.py biom
from biom import load_table
from biom.table import Table
import numpy as np
import sys

table = load_table(sys.argv[1])
a = table.nonzero_counts('observation',True)
b = table.ids(axis='observation')
print len(a)
print len(b)
for i in range(0,len(a)):
    print a[i],b[i]
