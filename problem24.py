from itertools import permutations

str1='0123456789'
perms = list( permutations(str1, len(str1)))

numbers = []
for p in perms:
    str1 = ''.join(p)
    numbers.append(str1)

numbers.sort()
print numbers[1000000-1]
