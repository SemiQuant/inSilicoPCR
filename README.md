# README

## In-Silico PCR tool

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7882322.svg)](https://doi.org/10.5281/zenodo.7882322)

This script takes a text file with primer sequence (one per line,optinal name in column 2, tab-seperated) and a reference FASTA file as input and identifies primer pairs which amplify a DNA sequence of length less than or equal to a user-specified maximum, at a given Tm and salt concentration. The script outputs the sequences of the primers, the portion of the primer that binds, the number of mismatches, as well as the start and end coordinates of the amplified sequence. It also outputs the Tm of the amplicons and the Tm of amplicon pairs.

### Dependencies

-   Python 3
-   [Biopython](https://biopython.org/)
-   [pandas](https://pandas.pydata.org/)
-   [BLAST+](https://www.ncbi.nlm.nih.gov/books/NBK569861/)

These may be installed by running

```
bash install.sh
```

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

#### in_silico_PCR.tsv
| qseq1   | qseq2_input          | qstart1 | qend1 | direction1 | mismatch2 | qseq2 | qseq1_input   | qstart2 | qend2 | direction2 | mismatch1 | binding_pos_diff | reference | ref_region |
|---------|----------------------|---------|-------|------------|-----------|-------|---------------|---------|-------|------------|-----------|------------------|-----------|------------|
| kkd_F_2 | gaacaccggcagtggttc   | 1       | 18    | +          | 0         | sge_R | ctgccgcagcggt | 1       | 13    | -          | 0         | 300              | example   | 772, 1072  |
| kkd_R   | accgagctgccggacggcac | 1       | 20    | +          | 0         | sge_R | ctgccgcagcggt | 1       | 13    | -          | 0         | 318              | example   | 772, 1090  |


#### in_silico_PCR_amplicon_interactions.tsv
| amplicon1_PF | amplicon1_PR | amplicon2_PF | amplicon2_PR | tm          |
|--------------|--------------|--------------|--------------|-------------|
| kkd_F_2      | sge_R        | kkd_R        | sge_R        | 90.22726832 |


#### in_silico_PCR_primer_dimears.tsv
| Sequence1 | Sequence2 | MeltingTemp       |
|-----------|-----------|-------------------|
| sge_F     | sge_R     | 75  |
| sge_F     | kkd_F     | 72 |
| sge_F     | kkd_F_2   | 73  |
| sge_F     | kkd_R     | 79 |
| sge_R     | kkd_F     | 74  |
| sge_R     | kkd_F_2   | 74 |
| sge_R     | kkd_R     | 80 |
| kkd_F     | kkd_F_2   | 72  |
| kkd_F     | kkd_R     | 78 |
| kkd_F_2   | kkd_R     | 78 |
