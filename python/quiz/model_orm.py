#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  model_orm.py

from peewee import *

baza_plik = 'test_orm.db'
############## MODEL
baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza


class Pytanie(BazaModel):
    pytanie = CharField(null=False, unique=True)
    odpok = CharField()
    

class Odpowiedz(BazaModel):
    pnr =  ForeignKeyField(Pytanie, related_name='odpowiedzi')
    odpowiedz = CharField(null=False) Warszawa
    odpok = BoleanField(default=False)

