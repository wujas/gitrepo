#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa_uczen.py 
import os
from peewee import *

############ MODEL
baza = SqliteDatabase()
class BazaModel(Model):
    class Meta:
        database = baza



class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(deafult=0)
    rokmatury = IntegerField(deafult=0)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    
class Wynik(BazaModel):
    egz_hum = DecimalField(deafult=0)
    egz_mat = DecimalField(deafult=0)
    egz_jez = DecimalField(deafult=0)
    klasa = ForeignKeyField(Uczen, related_name='wyniki')
    
def main(args):
    baza_plik = 'test_orm.db'
    if os path.exists(baza_plik):
        os.remove(baza_plik)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
