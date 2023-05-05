from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# packages = find_packages(include=['inSilicoPCR'])
dependencies = [
    'pandas',
    'biopython'
]

setup(
    name='PCRinSilico',
    version='0.0.13',
    url='https://github.com/SemiQuant/inSilicoPCR',
    install_requires=dependencies,
    description='In silico PCR tool',
    long_description=long_description,
    # long_description='This script takes a text file with primer sequence (one per line) and a reference FASTA file as input and identifies primer pairs which amplify a DNA sequence of length less than or equal to a user-specified maximum, at a given Tm and salt concentration. The script outputs the sequences of the primers, th eportion of the primer that binds, the number of mismatches, as well as the start and end coordinates of the amplified sequence.',
    long_description_content_type='text/markdown',
    author='Jason D Limberis',
    author_email='Jason.Limberis@ucsf.edu',
    keywords=['PCR', 'in silico PCR'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
