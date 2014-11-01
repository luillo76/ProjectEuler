def next_fibonacci(i,j):
    return i+j

def main():

    ndigits = 1000
    s = [1, 1]

    while( True ):
        s.append( next_fibonacci(s[-2], s[-1] ))
        if( len(str( s[-1])) >= ndigits ): 
            print len(s)
            break

    print s[-1]

if __name__ == '__main__':
    main()
