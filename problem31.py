def main():

    tot = 200

    ncomb = 0
    for i in range(0,tot+1,1):
        if( (i*1) > tot): break
        for j in range(0,tot+1,2):
            if( (i*1+j*2) > tot): break
            for k in range(0,tot+1,5):
                if( (i*1+j*2+k*5) > tot): break
                for l in range(0,tot+1,10):
                    if( (i*1+j*2+k*5+l*10) > tot): break
                    for m in range(0,tot+1,20):
                        if( (i*1+j*2+k*5+l*10+m*20) > tot): break
                        for n in range(0,tot+1,50):
                            if( (i*1+j*2+k*5+l*10+m*20+n*50) > tot): break
                            for o in range(0,tot+1,100):
                                if( (i*1+j*2+k*5+l*10+m*20+n*50+o*100) > tot): break
                                for p in range(0,tot+1,200):
                                    if( (i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200) > tot): break
                                    if( (i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200) == tot):
                                        ncomb += 1
                                        print i,j,k,l,m,n,o,p

    print ncomb

if __name__ == '__main__':
    main()
