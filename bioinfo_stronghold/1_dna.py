import collections

def countDNANeucleotides(seq):
    ntFreq = {'A':0, 'C':0, 'G':0, 'T':0} 
    for nt in seq:
        ntFreq[nt] += 1
    return ntFreq

f = open('RosalindProblems/ip_op/rosalind_dna.txt')
DNASeq = f.read().strip()

ans = countDNANeucleotides(DNASeq)
f.close()
print(' '.join([str(val) for key, val in ans.items()]))
    
        
