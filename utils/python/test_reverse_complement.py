#!/usr/bin/python

import sys
sys.path.append('./utils')
import reverse_complement

seq = "ATGCTat"
print seq
print reverse_complement.get_rc(seq)

seq_url = ">name\nATGTatn"
print seq_url
print reverse_complement.get_from_url(seq_url)
