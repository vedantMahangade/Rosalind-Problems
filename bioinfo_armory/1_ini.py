from Bio.Seq import Seq

f = open('rosalind_problems/bioinfo_armory/io/rosalind_ini.txt')
txt = f.read().strip()
dna_seq = Seq(txt)
print(dna_seq.count('A'), dna_seq.count('C'), dna_seq.count('G'), dna_seq.count('T'))

