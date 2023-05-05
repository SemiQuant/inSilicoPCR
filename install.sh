#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Installing it now..."
    sudo apt-get update
    sudo apt-get install python3
fi

# Create a virtual environment
python3 -m venv in_silico_pcr

# Activate the virtual environment
source in_silico_pcr/bin/activate

# Install Biopython and pandas using pip
pip install biopython pandas

# Download the BLAST+ binaries
wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.11.0+-x64-linux.tar.gz

# Unzip the BLAST+ binaries
tar -xzvf ncbi-blast-2.11.0+-x64-linux.tar.gz

# Add the BLAST+ binaries to the PATH
export PATH=$PATH:$(pwd)/ncbi-blast-2.11.0+/bin
