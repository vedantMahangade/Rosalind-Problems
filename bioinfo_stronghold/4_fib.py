def fibForRabbits(months, offsprings):
    if months == 1:
        return 1
    elif months == 2:
        return offsprings
    
    oneGenPrior = fibForRabbits(months-1, offsprings)
    twoGenPrior = fibForRabbits(months-2, offsprings)

    if months <= 4:
        return oneGenPrior + twoGenPrior
    
    return oneGenPrior + (twoGenPrior * offsprings)

f = open('rosalind_problems/bioinfo_stronghold/io/rosalind_fib.txt')
txt = f.read().strip().split(' ')
n = int(txt[0])
k = int(txt[1])
f.close()
print(fibForRabbits(n,k))
