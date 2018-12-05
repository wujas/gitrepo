#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#  Obliczanie potęgi liczby naturalnej


def potenga_re(a, n):
    if n == 0:
        return 1
    return potenga_re(a, n-1) * a
    
def potega_it(a, n):
    wynik = 1
    
    for i in range(n):
        wynik = wynik * a
        #print (wynik)

    return wynik

def main(args):
    a, n = 3, 0 # wielokrotne przypisanie
    print("Podstawa {} do potęgi {} wynosi {}".
           format(a, n, potega_it(a, n))) # wywołanie funkcji

    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))