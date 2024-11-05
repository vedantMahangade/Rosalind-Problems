def DNAtoRNA(DNASeq):
    RNASeq = DNASeq.replace('T','U',-1)
    return RNASeq

f = open('RosalindProblems/ip_op/rosalind_rna.txt')
DNASeq = f.read().strip()
f.close()
print(DNAtoRNA(DNASeq))