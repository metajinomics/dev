
import sys
sys.path.append('./utils')
import fetch_fasta

fetch_fasta.from_blast(sys.argv[1])

