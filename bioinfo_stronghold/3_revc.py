def reverseComplement(DNASeq):
    reverseSeq = ''
    for oldNT in DNASeq:
        newNT = oldNT
        if oldNT == 'A':
            newNT = 'T'
        elif oldNT == 'T':
            newNT = 'A'
        elif oldNT == 'G':
            newNT = 'C'
        elif oldNT == 'C':
            newNT = 'G'
        reverseSeq = newNT + reverseSeq
    return reverseSeq


f = open('RosalindProblems/ip_op/rosalind_revc.txt')
DNASeq = f.read().strip()
f.close()
print(reverseComplement(DNASeq))