#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma_cyfr.py
#  

def main(args):
    
    liczba = int(input("Podaj liczbę: "))
    while liczba < 10:
        print("Złe dane")
        liczba = int(input("Podaj liczbę: "))
    else:
        cyfry = list(map(int, str(liczba)))
    print ("Suma cyfr liczby:", sum(cyfry))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
