#this script compare two list then show different
#python compare_list.py list1 list2 

import sys

dict={}
for line in open(sys.argv[1],'r'):
    dict[line.strip()] = 0

for line in open(sys.argv[2],'r'):
    if not(dict.has_key(line.strip())):
        print "Not in list1: "+line.strip()
    else:
        dict[line.strip()] += 1

for item in dict.items():
    if (item[1] == 0):
        print "Not in list2: "+item[0]
