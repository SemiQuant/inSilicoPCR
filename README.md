# README

## In-Silico PCR tool

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7882322.svg)](https://doi.org/10.5281/zenodo.7882322)

This script takes a text file with primer sequence (one per line) and a reference FASTA file as input and identifies primer pairs which amplify a DNA sequence of length less than or equal to a user-specified maximum, at a given Tm and salt concentration. The script outputs the sequences of the primers, the portion of the primer that binds, the number of mismatches, as well as the start and end coordinates of the amplified sequence. It also outputs the Tm of the amplicons and the Tm of amplicon pairs.

### Dependencies

-   Python 3
-   [Biopython](https://biopython.org/)
-   [pandas](https://pandas.pydata.org/)
-   [BLAST+](https://www.ncbi.nlm.nih.gov/books/NBK569861/)

### Usage

```
python inSilicoPCR.py [options]
   --primer_seq [path to primer sequence file, one primer per line]
   --ref_fasta_file [path to reference FASTA file]
```

### Options

| Argument              | Description                                                  | Default      |
|-----------------------|--------------------------------------------------------------|--------------|
| `--annealing_temp`     | Annealing temperature (in Celsius).                           | 60.0         |
| `--salt_concentration` | Salt concentration (in nM).                                   | 50           |
| `--max_amplicon_len`   | Maximum length of PCR products in nucleotides.                | 2000         |
| `--req_five`           | Require the 5' end of the primer to bind?                      | True         |
| `--out_file`           | Output file name.                                             | "in_silico_PCR" |


### Example

```
python inSilicoPCR.py \
   --primer_seq ./example/primers.txt \
   --ref_fasta_file  ./example/ref.fasta
```


|qseq1             |qstart1|qend1|direction1|qseq2            |qstart2|qend2|direction2|mismatch1|mismatch2|binding_pos_diff|reference|
|:-----------------|------:|----:|:--------:|:----------------|------:|----:|:--------:|-------:|-------:|---------------:|---------------:|
|gaacaccggcagtggttc|      1|   18|    +     |ctgccgcagcggt     |      1|   13|    -     |       0|       0|             300|example        |
|accgagctgccggacggcac|      1|   20|    +     |ctgccgcagcggt     |      1|   13|    -     |       0|       0|             318|example      |


<!-- [Watch the video](geneblaze.gif") -->

