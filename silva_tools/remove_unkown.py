#!/usr/bin/python

import sys

flag = 0
for line in open(sys.argv[1],'r'):
    if line[:1] == ">":
        flag = 0
        if sys.argv[2] in line and "uncultured" not in line:
            print line,
            flag = 1
            
    else: 
        if flag == 1:
            print line.strip().replace("U","T")
    
    
