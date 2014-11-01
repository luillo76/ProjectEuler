from math import ceil

def isprime(number):
    if(number%2 == 0): return False
    
    i = 3
    while( i < int(ceil( (number+0.5)/2) )):
        if( number%i == 0): return False
        i += 2

    return True

def list_prime_factors(n_primes):

    primes = [2]

    i = 3
    while( len(primes) < n_primes ):
        if( isprime(i) ):
            primes.append( i )
            print len(primes), primes[-1]

        i += 2

    return primes

def main():

    n = 10001
    print list_prime_factors(n)

if __name__ == '__main__':
    main()
