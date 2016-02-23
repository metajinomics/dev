## get_percent_b_merge.py
This script help you find percent of coverage of you primer when you use cdhit before run PrimerDesign

You need to have following files

cdhit.prot.seqs.inti1.fa.clstr <- clustar file which is output of cd-hit

output of PrimerDesign
Primer.Party_SeqscoveredUniform1
Primer.Party_SeqscoveredUniform2
Primer.Party_SeqscoveredUniform3
Primer.Party_SeqscoveredUniform5
Primer.Party_SeqscoveredUniform10

then run
```
python get_percent_b_merge.py Primer.Party_SeqscoveredUniform cdhit.prot.seqs.inti1.fa.clstr
```
then you can see the result:
```
1 pair 3927 / 5005	78 %
2 pair 3929 / 5005 	78 %
3 pair 3934 / 5005 	78 %
5 pair 3963 / 5005 	79 %
10 pair 3969 / 5005 	79 %
```

