
import sys
sys.path.append('./utils')
import fetch_fasta

fetch_fasta.from_multi_blast(sys.argv[1])

