## assembly downstream
This script help downstream process after assembly

## what you expect before start
You have done assembly, mapping, counting

see here,  https://github.com/metajinomics/automation

If you submit your assembly to MG-RAST, you can get annotated file. (eg. mgmxxxx_function_KEGG.tab, mgmxxxx_organism_KEGG.tab)

## merge each counting into one
See here, https://github.com/germs-lab/coverage_count

### if you want, you can make another fasta file based on annotation (CDS assignment)
~~~
java get_each_gene_fasta.java assembly 350.faa output.fna
~~~

## add annotation ec number and taxonomy
At this point, I expect you have tree files, normal_counts.txt, mgmxxxx_function_KEGG.tab, mgmxxxx_organism_KEGG.tab .

