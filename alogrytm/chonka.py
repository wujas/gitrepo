#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  


def main(args):
    
    h = int(input("Podaj wysokość choinki: "))
    b = 0
    znak = input("Podaj znak, którym chcesz rysować: ")
    
    while b<h :
        c = b + 1
        while c > 0:
            print(znak, end = '')
            c = c - 1
        b = b + 1
        print()
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
