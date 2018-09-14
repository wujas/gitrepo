#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunki .py

#def maks(a, b. c):
 #   pass
  #  return maks

def main(args):
    
    a = int(input("Podaj 1 liczbę: "))
    print(a)
    b = int(input("Podaj 2 liczbę: "))
    print(b)
    c = int(input("Podaj 3 liczbę: "))
    print(c)
    
    if b <= a >= c:
        print(a," jest największe")
    elif a <= b >= c:
        print(b, "jest największe")
    else:
        print(c, "jest największe")
    
   # assert(maks(3, 2, 1) == 3)    
   # assert(maks(3, 3, 1) == 3)    
   # assert(maks(3, 2, 3) == 3)    
   # assert(maks(3, 1, 3) == 3)    
   # assert(maks(3, 1, 1) == 3)    
   # assert(maks(3, 3, 1) == 3)    
   # assert(maks(3, 3, 3) == 3)    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
