#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#
# Obliczanie potęgi liczby naturlnej

def potenga_it(a, n):
    wynik = 1
    for i in range(n):
        wynik = wynik * a
    
    return wynik
    
def potenga2_it(a, n):
    
    print(a**n)
    
    
def main(args):
    a = int(input("Podaj liczbę: "))
    n = int(input("Podaj wykładnik: "))
    
    print("Podstawa {} do potęgi {} wynosi {}".
            format(a, n, potenga_it(a, n)))
    # potenga_it(a, n)    # Wywołanie funkcji
    


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
