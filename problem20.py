from math import ceil, sqrt

def factorial(n):
    if(n==1): return 1
    
    return n*factorial(n-1)

def main():

    n = 100
    result = factorial(n)

    result = list(str(result))
    result = map(int, result)

    print result
    total = sum(result)
    print total

if __name__ == '__main__':
    main()
