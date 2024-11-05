from sequences import *
from collections import Counter

def validate_dna_sequence(seq):
    '''Returns the sequence itself if valid (countains only ACGT), else returns 'false' '''
    seq = seq.upper()
    for alphabet in seq:
        if alphabet not in neucleotides_dna:
            return "false"
    return seq

def count_dna_neucleotides(seq):
    '''Returns the an object of type 'dict' with frequency for each neucloetide'''
    ntFreq = {'A':0, 'C':0, 'G':0, 'T':0} 
    for nt in seq:
        ntFreq[nt] += 1
    return ntFreq

def transcribe_dna(seq):
    '''Returns the transribed RNA sequence for the input DNA sequence by replacing Thyamine (T) with Uracil (T)'''
    rna_seq = seq.replace('T','U')
    return rna_seq

def reverse_complement(seq):
    '''Returns the Reverse Complement of the input DNA sequence'''
    # reverse_seq = ''.join([reverse_complement_dna[nuc] for nuc in seq])[::-1]
    # return reverse_seq
    mapping = str.maketrans('ATCG','TAGC')
    return seq.translate(mapping)[::-1]

def calculate_gc_content(seq):
    '''GC Content in a given DNA/RNA sequence'''
    seq = seq.upper()
    return ((seq.count('G') + seq.count('C'))/len(seq))*100

def calculate_gc_content_subset(seq, k = 10):
    '''GC Content in a given DNA/RNA sub-sequence of lenght k (default: 10)'''
    res = []
    for i in range(0, len(seq)-k+1, k):
        subseq = seq[i: i+k]
        res.append(calculate_gc_content(subseq))
    return res

def translate_dna(seq, init_pos=0):
    '''Translates a DNA sequence seq into amino acids'''
    return [dna_codons[seq[pos: pos+3]] for pos in range(init_pos, len(seq) -2, 3)]

def codon_usage_frequency(seq, amino_acid):
    '''Teturns the frequency of different codon in the sequence for a given amino acid'''
    codons = []
    for i in range(0, len(seq)-2, 3):
        if dna_codons[seq[i:i+3]] == amino_acid:
            codons.append(seq[i:i+3])

    codonFrequency = dict(Counter(codons))
    totalWeight = sum(codonFrequency.values())

    for codon in codonFrequency:
        codonFrequency[codon] = round(codonFrequency[codon]/totalWeight, 2)
    return codonFrequency