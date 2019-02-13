#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kodmorse.py

kod = {'A': '+-', 'B': '-+++', 'C': '-+-', 'D': '-++', 'E': '+',
    'F': '++-+', 'G': '--+', 'H': '++++', 'I': '++', 'J': '+---',
    'K': '-+-', 'L': '+-++', 'M': '--', 'N': '-+', 'O': '---',
    'P': '+--+', 'Q': '--+-', 'R': '+-+', 'S': '+++', 'T': '-',
    'U': '++-', 'V': '+++-', 'W': '+--', 'X': '-++-', 'Y': '-+--',
    'Z': '--++', 'Ą': '+-+-', 'Ć': '-+-++', 'Ę': '++-++',
    'Ł': '+-++-', 'Ń': '--+--', 'Ó': '---+', 'Ś': '+++---+++',
    'Ż': '--++-+', 'Ź': '--++-'}



def koduj(tekst):
    for l in tekst:
        print(kod[l])
        

def dekoduj():
    tekst = []
    lit = ' '
    while lit > '':
        lit = input('Podaj tekst: ')
        tekst.append(lit)
    print(tekst)
    
    
def main(args):
    # ~tekst = input('podaj tekst: ').lower()
    # ~print("".join([kod[l] for l in tekst]))
    dekoduj()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
