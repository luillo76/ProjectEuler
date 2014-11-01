import operator

def main():

    sum = 1000

    for a in range(1,1000):
        for b in range(a,1000):
            c = sum -a -b
            if(c<=b): continue
            if(a*a + b*b == c*c):
                print a, b, c, a*b*c

if __name__ == '__main__':
    main()
