import sys

def sum(a,b) :
    c = a+b
    return c

if __name__ == '__main__':
    args = sys.argv
    d = sum(int(args[2]),int(args[4]))
    print (d)
   