from toolkit import *
from sequences import *
import random

random_dna_seq = ''.join([random.choice(neucleotides_dna) for nuc in range(50)])

dna_seq = validate_dna_sequence(random_dna_seq)

print(f'\n[0] + Sequnce: {dna_seq}\n')
print(f'[1] + Sequence Length: {len(dna_seq)}\n')
print(f'[2] + Neucleotide Frequency: {count_dna_neucleotides(dna_seq)}\n')
print(f'[3] + Transcribed DNA (RNA): {transcribe_dna(dna_seq)}\n')
print(f'[4] + Sequence + Complement + Reverse Complement:')
print(f"\t5` {dna_seq} 3` [sequence]")
print(f"\t   {''.join(['|' for c in range(len(dna_seq))])} ")
print(f"\t3` {reverse_complement(dna_seq[::-1])} 5` [complement]")
print(f"\t5` {reverse_complement(dna_seq)} 3` [reverse complement]\n")
print(f'[5] + GC Content: {calculate_gc_content(dna_seq)}%\n')
print(f'[6] + GC Content for sub sequences of length 5: {calculate_gc_content_subset(dna_seq, k=5)}%\n')
print(f'[7] + Translated DNA (Amino Acids) initiating from position {0}: {translate_dna(dna_seq, init_pos=0)}\n')
print(f'[8] + Codon Frequency for amino acid (A): {codon_usage_frequency(dna_seq,"A")}\n')



# DNASeq = 'TCGTACTGAAAATTAACCCTCGGGGTTCAAACCCTGGCCCGTCTTCCTCTCTATGTGAAGAACCAAAAGGAATCTAGCTAGCACTGGTCCTAGAATTGATCGTTAATTGCAACTTCGGCGAGTAGCTCGAGTAATTGAAACCCGCATGTATAAGCATCATCCCCCTCGCAATAGCCCGTACGCAAGCGCATCCCGATCATACATTCAACCACACCTGCGTCACGCACTAATGATCCCGTGAGCGCCACAACGGGCCGTGTAAGACAGCTATCATGGCGGACTCTTATCTTGGAACGCTCATTACCGCGACGACTAACGCGGCCGCGCTGTGTCCTCGGCGTCGTTCGTCTTGGACTCGTGGATTTGCGGTGGGTACTTCTTTGCGGTAAACGAGCTCTACATTTCAACCTACTAGGTAACTCCCTCCGGGCTTGCTTTATGGCGATGGGAAGAAATCTGAATCCCCTCTTACAACTTGGTTTCCTTCTCGCCAGCGTGACCGTCTCAAATCAATCCGTATCCTATTTACGTTAATCATTTGTACCATCAGTGGAACGAGTAACTGTGAGCCCGATGGTTCCTGTAGCAGGACTTTTGAATTACTGGTTTGATGTGTTAAATATGTAGAGCCAGTGTTTACCCATCCCTGAAAAAAGGTGTAATTGTCTTCGCAGCCTATTGAATCTATCGGGCCACCTGGGATTTTATTAAAGTGCCTTCCACGACCATAATAATCGATCTTTATCTATCAGCGAAGGTGGCCCAGAGAATAGGTGTACGGACAATCGCTCCCATTCGCATTAGCAAACGCGAGTGCTATCTGGGCTAAGGGGAATTAGGGCCTACGATAGCAGGTTAACTAGGCTTATATAACCATCGCGCCTGAGTAGGCCGCATGATGAAGTGTGCACGGCGATTACATCTTACGGGTGATAGCAATTTAGCTATTACCGAGAATAGTTCTCATCGG'

# print(validateDNADataset(DNASeq))
# print(countDNANeucleotides(DNASeq))
# print(DNAtoRNA(DNASeq))