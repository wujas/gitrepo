#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  siema.py
#  

def main(args):
    a = str(input('Jak masz na imie?: '))
    b = str(input('Jak masz na nazwisko?: '))
    
    print("Witaj", a,b)
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
