from math import ceil

def list_of_primes(number):
    list = [2]

    for i in range(3,number,2):
        isprime = True
        maxFactor = int(ceil( (i+0.5)/2) )

        for div in range(2,maxFactor):
            if(i%div==0):
                isprime = False
                break
        if(isprime): list.append(i)

    return list

def list_prime_factors(number):

    factors = []

    if(number%2==0): factors.append(2)

    i = 3
    while(True):
        if(i>number//2): break

        isprime = True
        maxFactor = int(ceil( (i+0.5)/2) )
        div = 2

        while(True):
            div += 1
            if(div > maxFactor): break
            if(i%div==0):
                isprime = False
                break

        if(isprime and number%i==0): 
            factors.append(i)
            product = reduce(lambda x, y: x*y, factors)
            if(product >= number): break

        i += 2

    return factors

def main():

    #n = 13195
    n = 600851475143
    
    print list_prime_factors(n)

if __name__ == '__main__':
    main()
