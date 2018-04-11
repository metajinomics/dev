

### rarefy individual file
```
python rarefy.py sample_R1_001.fastq 50000 > sample.50000.fastq
```

### rarefy paired end
```
python rarefy_paired_read.py sample_R1_001.fastq sample_R2_001.fastq 50000
```

### rarefy paired end and interleave
```
python rarefy_paired_read_and_interleave.py sample_R1_001.fastq sample_R2_001.fastq 50000 > sample.interleaved.50000.fastq
```

### inteleave paired end
```
python interleave.py sample_R1_001.fastq sample_R2_001.fastq > sample.interleaved.fastq
```
