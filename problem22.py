def main():

    abc = {'a':1,
           'b':2,
           'c':3,
           'd':4,
           'e':5,
           'f':6,
           'g':7,
           'h':8,
           'i':9,
           'j':10,
           'k':11,
           'l':12,
           'm':13,
           'n':14,
           'o':15,
           'p':16,
           'q':17,
           'r':18,
           's':19,
           't':20,
           'u':21,
           'v':22,
           'w':23,
           'x':24,
           'y':25,
           'z':26,
       }

    with open("p022_names.txt") as f:
        line = f.readline()

    names = line.split(',')
    names = [s.strip('"') for s in names]
    names.sort()

    grand_total = 0
    for x in names:

        index = names.index(x)
        result = list(str(x.lower()))

        total = 0
        for l in result:
            total += abc[l]

        grand_total += (index+1)*total

    print grand_total

if __name__ == '__main__':
    main()
