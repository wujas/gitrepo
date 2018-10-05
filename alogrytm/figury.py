#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  




def choinka(h, znak):


    h = int(input("Podaj wysokość choinki: "))
    znak = str(input("Podaj znak, którym chcesz rysować: "))
    
    for i in range(h):
        for j in range(i + 1):
            print(znak, end = '')
        print()
        
    return 0
def choinka2(h, znak):


    h = int(input("Podaj wysokość choinki: "))
    znak = str(input("Podaj znak, którym chcesz rysować: "))
    
    for i in range(h):
        for j in range(h - i):
            print(znak, end = '')
        print()
        
    return 0
        
def prostokat1(a, b, znak):
    
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))    
    znak = str(input("Podaj znak budujący prostokąt: "))    
    
    i = 0
    j = 0
    

    for i in range(a):
        for j in range(b):
            if j == 0 and j == b - 1:
                print(znak , end='')
            else:
                print("")
        
        print()
        



def tro(a, b, znak):
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))    
    znak = str(input("Podaj znak budujący prostokąt: "))    
    
    i = 0
    j = 0
    

    for i in range(a):
        for j in range(b):
            print(znak , end='')
        print()
    
    
def trojkat(h, znak)
    
    h = int(input("Podaj wysokość choinki: "))
    znak = str(input("Podaj znak, którym chcesz rysować: "))
    
    for i in range(h):
        for j in range(h - i):
            print(znak, end = '')
        print()
        
    return 0
    
    
def main(args):
    h, znak = 6, "#"
    trojkat(h, znak)
    print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
