
#python tsv_rev_comp.py input > output

import sys
import reverse_complement

for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    if not spl[3] == "-":
        r = reverse_complement.get_rc(spl[3])
        spl[3] = r
    print '\t'.join(spl)
    
