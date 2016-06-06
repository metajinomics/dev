#!/usr/bin/python
# python get_seq_fastq.py seq.fa start end
import sys
fread = open(sys.argv[1],'r')
fread.next()

with fread as f:
    seq =  "".join(line.strip() for line in f)
start = int(sys.argv[2])
end = int(sys.argv[3])
print seq[start-1:end]
