from itertools import permutations

str1='123456789'
perms = list( permutations(str1, len(str1)))

numbers = []
for p in perms:
    str1 = ''.join(p)
    numbers.append(str1)

for i in numbers[:10]:
    print i
    for j in range(1,(len(i))):
        print i[:j]

