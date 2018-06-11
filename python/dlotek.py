#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileliczb = int(input("Ile liczb wytypujesz? "))
    maksliczba = int(input("Podaj maksymalna losowana liczbe: "))
    print("Wytypuj {} z {} liczb: ".format(ileliczb, maksliczba))

    liczby = []   # definicja pustej listy na losowane liczby
    i = 0  # licznik unikalnych wylosowanych liczb
    # for i in range(ileliczb):
    while i < ileliczb:
        liczba = random.randint(1, maksliczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i += 1  # powieksz liczbik o 1
    print("Wylosowano:", liczby)

    typy = set()  # def. pustego zbioru na typy uzytkownika
    i = 0  # licznik uniklh=nych typow uzytkownika
    while i < ileliczb:
        typ = input("Podaj liczbę {}: ".format(i + 1))
        if typ not in typy:
            typy.add(typ)
            i += 1
    print("Wytypowane: ", typy)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
