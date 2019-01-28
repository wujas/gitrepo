#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  forms.py

from flask_wtf import FlaskFrom
from wtforms import HiddenField, StringField, BooleanField
from wtforms import SelectField, FormField, FieldList
from wtforms.validators import Required

blad1='To Pole jest wymagane!'

class OdpForm(FlaskForm):
    id = HiddenField()
    pytanie = HiddenField()
    odpowiedź = StringField('Odpowiedź:', validators=[Required(message=blad1)])
    odpok = BooleanField('Poprawna:')
    
    
class DodajForm(FlaskForm):
    pytanie = StringField('Treść pytania:', validators[Required(massage=blad1)])
    kategorie = SelecyField('Kategoria', coerce=int)
    odpowiedzi = FieldList(FormField(OdpForm), min_entries=3)
    id = HiddenField()
