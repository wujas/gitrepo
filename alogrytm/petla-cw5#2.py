#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-cw5#2.py
#  
#DANE WEJŚCIOWE:
#liczby dodatnie podawane przez uzytkownika
#DANE WYJŚCIOWE:
#suma liczb podanych przez uzytkownika
#program musi zapewnosc poprawnosc danych
# program konczy dzialanie po wprowadzeniu wartosci 0


def main(args):
    
    suma = 0
    liczba = -1
    
    while liczba != 0:
        liczba = int(input("Podaj liczbę: "))    
        while liczba < 0: #pętla zaporowa
            liczba = int(input("Błędne dane!" , end=''))
        else:
            suma += liczba
    
    print("Suma: ", suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
