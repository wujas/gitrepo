#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py

def trojkat(a, b, c):
    
    
    if a + b > c and b + c > a and c + a >b:
        return True
    
    return False

def main(args):

    assert(trojkat(3, 4, 5) == True)
    assert(trojkat(3, 4, 1) == False)
    
    # ~a = int(input("Podaj 1 bok: "))
    # ~print(a)
    # ~b = int(input("Podaj 2 bok: "))
    # ~print(b)
    # ~c = int(input("Podaj 3 bok: "))
    # ~print(c)
    
    # ~if trojkat(a, b, c):
        # ~print("da sie")
    # ~else:
        # ~print("nie da sie")
   
    
   
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
