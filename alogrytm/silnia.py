#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#
# Obliczanie silni liczby naturlnej

def silnia_it(n):
    """
    n! = 1 * 2 * ... * n
    """
    wynik = 1
    
    for i in range(n):
        wynik = wynik * i 
        
    
    return wynik
    
def potenga2_it(a, n):
    
    print(a**n)
    
    
def main(args):
    n = int(input("Podaj silnie: "))
    
    print("{}! silnia wynosi {}".
            format(n, silnia_it(n)))
    # potenga_it(a, n)    # Wywołanie funkcji
    


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
