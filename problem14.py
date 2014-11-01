import math

def collatz(n):
    if(n%2 == 0):
        return int(math.floor((n+0.5)/2))
    else:
        return 3*n+1

def getCollatz(n):
    list = [n]
    while( n!= 1):
        n = collatz(n)
        list.append(n)

    return list

def main():

    n = 0
    f = 0

    max = 1000000
    for i in range(1,max+1):
        arr = getCollatz(i)
        #print arr
        if(n<len(arr)): n,f = len(arr), arr[0]

    print n,f

if __name__ == '__main__':
    main()
