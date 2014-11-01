a,b=2,100

arr = []
for i in range(a,b+1):
    for j in range(a,b+1):
        arr.append(i**j)

arr = list(set(arr))
print len(arr)
