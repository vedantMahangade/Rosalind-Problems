neucleotides_dna = ['A', 'C', 'G', 'T']
neucleotides_rna = ['A', 'C', 'G', 'U']
# reverse_complement_dna = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

dna_codons = {
    # 'M' - START, '_' - STOP
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', # (Ala/A) Alanine 
    'TGT': 'C', 'TGC': 'C',     # Cysteine (Cyc) - p
    'GAT': 'D', 'GAC': 'D',     # (Asp/D) Aspartic acid 
    'GAA': 'E', 'GAG': 'E',     # (Glu/E) Glutamic acid 
    'TTT': 'F', 'TTC': 'F',     # (Phe/F) Phenylalanine 
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',     # (Gly/G) Glycine 
    'CAT': 'H', 'CAC': 'H',     # (His/H) Histidine 
    'ATA': 'I', 'ATT': 'I', 'ATC': 'I',     # (Ile/I) Isoleucine
    'AAA': 'K', 'AAG': 'K',     # (Lys/K) Lysine 
    'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',     # (Leu/L) Leucine
    'ATG': 'M',     # Met/M) Methionine 
    'AAT': 'N', 'AAC': 'N',     # (Asn/N) Asparagine 
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',     # (Pro/P) Proline
    'CAA': 'Q', 'CAG': 'Q',     # (Gln/Q) Glutamine 
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',     # (Arg/R) Arginine (
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S',     # (Ser/S) Serine
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',     # (Thr/T) Threonine 
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',     # (Val/V) Valine
    'TGG': 'W',     # (Trp/W) Tryptophan 
    'TAT': 'Y', 'TAC': 'Y',     # 	(Tyr/Y) Tyrosine 
    'TAA': '_', 'TAG': '_', 'TGA': '_'      # STOP
}
