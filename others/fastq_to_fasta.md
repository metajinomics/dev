```
for x in *.fastq;do cat $x | paste - - - - | sed 's/^@/>/g'| cut -f1-2 | tr '\t' '\n' > ${x%.fastq*}.fasta;done
```
