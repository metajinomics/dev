import sys
import reverse_complement
for line in open(sys.argv[1],'r'):
    if(line[:1]==">"):
        print line.strip()+"_rc"
    else:
        rc = reverse_complement.get_rc(line.strip())
        print rc
