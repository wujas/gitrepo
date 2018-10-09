#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#

def trojkat(h, znak):
    t = (h-1)*2
    for i in range(h-1, -1, -1):
        for j in range(t+1):
            if j < i or j > t-i:
                print(" ", end='')
            else:
                print(znak, end='')
        print()


def main(args):
    h = int(input("Podaj wysokosc trójkąta: "))
    z = input("Podaj znak: ")

   

    trojkat(h, z)

    return 0
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
