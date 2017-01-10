#!/usr/bin/python
#usage: python cp_file.py list64.txt small64/

import sys
import os
#read
di = sys.argv[2]
for line in open(sys.argv[1],'r'):
    command = "cp "+line.strip()+"* " + di
    #print command
    os.system(command)
