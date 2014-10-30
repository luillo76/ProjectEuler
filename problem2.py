def fibonacci(arr):
    return arr[-1] + arr[-2]

def main():

    arr = [ 1, 2 ]

    while(True):
        last = fibonacci(arr)
        if(last>4000000): break
        arr.append(last)

    sum = 0
    for i in arr:
        if(i%2==0): sum += i

    print "sum = ", sum

if __name__ == '__main__':
    main()
