from math import ceil, sqrt

def isprime(number):
    if(number%2 == 0): return False
    
    maxint = ceil( sqrt(number) )
    i = 3
    while( i <= maxint ):
        if( number%i == 0): return False
        i += 2

    return True

def list_prime_factors(maxprime):

    primes = [2]

    last=0
    i = 3
    while( primes[-1] < maxprime ):
        if( isprime(i) ):
            primes.append( i )
        if ( len(primes)%10000 == 0) and (last!=primes[-1]):
            last = primes[-1]
            print last, len(primes)

        i += 2

    return primes

def main():

    n = 2000000
    list = list_prime_factors(n)

    print " -> ", sum(list[:-1])

if __name__ == '__main__':
    main()
