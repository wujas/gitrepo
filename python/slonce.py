#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  slonce.py
#  

import turtle as t

def figura(bok, kat, ile):
    for i in range(ile):
        t.forward(bok)
        t.right(kat)


def figura_rek(bok, kat, ile, krok):
    # ~t.right(kat)
    t.forward(bok)
    t.right(kat)
    print(ile)
    if ile > 0: # warunek brzegowy
        figura_rek(bok, kat + krok, ile - 1, krok)
    
    
def main():
    t.setup(800, 600)
    t.color('red', 'black')
    t.begin_fill()
    t.speed(5)
    
    figura_rek(200, 50, 18, 10)
    
    t.end_fill()
    t.done()
    return 0

main()
