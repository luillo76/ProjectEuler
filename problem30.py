def get_sum(number,power):
    results = list(str(number))
    results = map(int, results)
    if(len(results) == 1): return -1

    results =  [x**power for x in results]
    return sum(results)
def main():

    power = 5
    maxint = 9**power*power
    print " max -> ", maxint
    
    grand_total = 0
    for i in range(0,maxint):
        tot =  get_sum(i, power)
        if(tot == i):
            print i
            grand_total += i

    print " tot -> ", grand_total

if __name__ == '__main__':
    main()
