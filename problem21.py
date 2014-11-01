from math import ceil

def list_factors(n):

    maxint = int( ceil( (n+0.5)/2 ) )

    factors = []
    for i in range(1,maxint):
        if( n%i==0 ): factors.append(i)
    return factors

def main():

    tot = 0
    for a in range(1, 10001):

        fa = list_factors(a)
        b = sum(fa)
        fb = list_factors(b)
    
        if(a==sum(fb)) and (a!=b):
            tot += (a+b)
            print a, b, sum(fb)

    # magagna
    print tot/2

if __name__ == '__main__':
    main()
