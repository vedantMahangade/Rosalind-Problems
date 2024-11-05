
# INI1: Installing Python
import this


# INI2: Variables and Some Arithmetic
f = open('rosalind_problems/python_village/io/rosalind_ini2.txt','r')
txt = f.read().strip().split(' ')
a = int(txt[0])
b = int(txt[1])
c = a**2 + b**2
print(c)
f.close()

# INI3: Strings and Lists
f = open('rosalind_problems/python_village/io/rosalind_ini3.txt','r')
txt = f.readline().strip()
nums = f.readline().strip().split(' ')
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
d = int(nums[3])
s1 = txt[a:b+1]
s2 = txt[c:d+1]
print(s1,s2)
f.close()


# INI4: Conditions and Loops
f = open('rosalind_problems/python_village/io/rosalind_ini4.txt','r')
txt = f.read().strip().split(' ')
a = int(txt[0])
b = int(txt[1])
sum=0
if a%2==0:
    a=a+1
for i in range(a,b+1,2):
    if i%2 != 0:
        sum = sum+i
print(sum)
f.close()


# INI5: Working with Files
f = open('rosalind_problems/python_village/io/rosalind_ini5.txt','r')
op = open('rosalind_problems/python_village/io/outputFile.txt','w')
lineNo = 1
while True:
    line = f.readline()
    if not line:
        break
    if lineNo % 2 == 0:
        op.write(line)
    lineNo += 1
f.close()
op.close()


# INI6: Dictionaries
f = open('rosalind_problems/python_village/io/rosalind_ini6.txt','r')
words = f.read().strip().split(' ')
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
for key, value in freq.items():
    print(key, value)
f.close()