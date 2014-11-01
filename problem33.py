from fractions import gcd

fnum = 1
fden = 1

for i in range(10,100):
    for j in range(i+1,100):
        #if(i==49) and (j==98):

        num = map(int, list(str(i)))
        den = map(int, list(str(j)))

        common =  list(set(num) & set(den))
        if( len(common) ==0 ): continue
        if( common[0] == 0): continue
            
        num1 = list(set(num) - set(common))
        den1 = list(set(den) - set(common))

        if(len(num1) == 0): continue
        if(len(den1) == 0): continue

        num1 = ''.join(str(e) for e in num1)
        den1 = ''.join(str(e) for e in den1)

        num1 = int(num1)
        den1 = int(den1)

        if(num1==0): continue
        if(den1==0): continue
            
        if( float(i)/j == float(num1)/den1):
            print i, j, num1, den1
            fnum *= i
            fden *= j

print fnum, fden, gcd(fnum, fden), fden/gcd(fnum, fden)
