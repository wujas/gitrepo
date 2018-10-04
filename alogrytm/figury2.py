#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  

def main(args):
    
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))
    znak = input("Podaj znak, którym chcesz rysować: ")
    
    i = 0
    j = 0
    
    for i in range(a):
        if i == 0 or i == a-1:
            print(znak * a)
            continue
        for j in range(b):
            if j > 0 and j < b - 1:
                print(" ", end = '')
            else:
                print(znak, end = '')
    
print()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
