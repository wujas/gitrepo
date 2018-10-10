#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py


def liczby2():
    """
    Funkcja drukuje wszystkie liczby 2 cyfrowe
    w których cyfry nie powrarzają się. Funkcja zwraca
    ich liczbę. Wykluczone liczby 11, 22, 33, itd.
    """
    
    
    i = 0
    j = 0
    
    ile = 0 # licznik
    
    for i in range(1,10): # pętla zewnetrzna
        for j in range(0, 10): # pętla wewnetrzna
            if i != j:
                print("{}{}  ".format(i, j), end='')
                ile = ile + 1
        
    return 0
    
    

def main(args):
    print("Liczb 2-cyfrowych: ", liczby2())

    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
