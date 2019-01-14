```
for x in *.fastq;do cat $x | paste - - - - | sed 's/^@/>/g'| cut -f1-2 | tr '\t' '\n' > ${x%.fastq*}.fasta;done
```

```
for x in *.fastq;do cat $x | paste - - - - | awk 'BEGIN{FS="\t"}{print ">"substr($1,2)"\n"$2}' > ${x%.fastq*}.fasta;done
```
