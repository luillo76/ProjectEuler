from math import ceil
import numpy as np

def main():

    n = 100

    x = np.array( range(1,n+1) )
    x2 = x*x

    print np.sum(x)*np.sum(x) - np.sum(x2)

if __name__ == '__main__':
    main()
