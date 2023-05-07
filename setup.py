from setuptools import setup, find_packages
from setuptools.command.install import install
from pathlib import Path
import os

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# packages = find_packages(include=['inSilicoPCR'])
dependencies = [
    'pandas',
    'biopython'
]

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        os.system("wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.14.0/ncbi-blast-2.14.0+-x64-linux.tar.gz")
        os.system("tar -xzvf ncbi-blast-2.11.0+-x64-linux.tar.gz")
        os.system("export PATH=$PATH:%s" % os.path.abspath("$(pwd)/ncbi-blast-2.11.0+/bin"))


setup(
    name='PCRinSilico',
    version='1.0.2',
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
    entry_points={
        'console_scripts': [
            'PCRinSilico=PCRinSilico.PCRinSilico:main',
        ],
    },
    cmdclass={
        'install': CustomInstallCommand,
    }
)

