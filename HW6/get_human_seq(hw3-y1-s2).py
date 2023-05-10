from Bio import Entrez, SeqIO
import random
import json
import numpy as np


def get_seq():
    Entrez.email = ""  # Set your email address

    # choose chromosome id from https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.40

    chr_id = "CM000686"  # chrY

    # retrieve sequence for chromosome
    handle = Entrez.efetch(db="nucleotide", id=chr_id, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")

    i = 1
    while i < 100:
        # choose random position and extract 100 bp fragment

        start = random.randint(0, len(record.seq) - 100)
        end = start + 100
        fragment = record.seq[start:end]
        if 'N' in fragment:
            continue
        else:
            print(">fragment_" + str(i + 1))
            print(fragment)
            i += 1


def parse():
    res = []

    with open('Files/human-alignment.json') as f:
        results = json.load(f)

    # Iterate over each read in the results
    for read in results['BlastOutput2']:
        read_name = read['report']['results']['search']['query_title']

        hits = [hit for hit in read['report']['results']['search']['hits']]  # 0 for all

        # Get the top hit and extract the scientific name
        if hits:
            top_identity = hits[0]['hsps'][0]['identity']

            res.append(top_identity)

    print(res)
    print(np.mean(res))