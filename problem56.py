maximum = 0
for i in range(1,100):
    for j in range(1,100):
        #results = list(str(i**j))
        #results = map(int, results)
        #value = sum(results)
        value = sum(int(v) for v in str(i**j))

        if(maximum < value): maximum = value

print maximum

