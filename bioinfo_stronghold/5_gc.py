import math

def readFileAndCalculate():
    f = open('rosalind_problems/bioinfo_stronghold/io/rosalind_gc.txt', 'r')
    line = f.readline().strip()
    dna_seq = {}
    while True:
        if not line:
            break
        if line.startswith('>'):
            id = line.replace('>','')
            nextLine = f.readline().strip()
            seq = ''
            while True:
                if nextLine.startswith('>') or not nextLine:
                    line = nextLine
                    break
                else:
                    seq = seq + nextLine
                nextLine = f.readline().strip()
            
            dna_seq.update({id: calculate_gc_content(seq)})
    f.close()
    return dna_seq

def calculate_gc_content(seq):
    seq = seq.upper()
    gc_content = ((seq.count('G') + seq.count('C'))/len(seq))*100
    return round(gc_content, 6)


dna_seq = readFileAndCalculate()

maxKey = max(dna_seq,key=dna_seq.get)

print(f'{maxKey}\n{dna_seq[maxKey]}')





