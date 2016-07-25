import sys

for n,line in enumerate(open(sys.argv[1],'r')):
    print ">" + str(n)
    print line,
