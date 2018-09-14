#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunki .py


def main(args):
    
    a = int(input("Podaj 1 liczbę: "))
    print(a)
    b = int(input("Podaj 2 liczbę: "))
    print(b)
    
    if a > b:
        print(a, "jest większe", b)
    elif b > a:
        print(b, "jest większe", a)
    else:
        print(b, "równa się", a)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
