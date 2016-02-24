#!/usr/bin/python

import sys
sys.path.append('./utils')
import read_rdp_taxonomy

filename = sys.argv[1]
tax = read_rdp_taxonomy.get_tax(filename)
print tax
