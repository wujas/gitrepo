#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza.py
#  
#  Copyright 2018  <>





def dodaj_dane(dane):

    for model, plik in dane.items():
        pola = [pole for pole in model._meta.fields]
        pola.pop(0)
        wpisy = dane_z_pliku(plik + '.csv')
        with baza.atomic():
            model.insert_many(wpisy, fields=pola).execute()
            
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
