#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
#
import sqlite3



def kwerenda(cur):
    cur.execute("""
        WITH srednie AS (
            SELECT nazwisko, imie, AVG(ocena) AS sred FROM uczniowie
            INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
            GROUP BY uczniowie.id
        ) SELECT nazwisko, imie, sred FROM srednie
            WHERE sred > 3.5 ORDER BY sred DESC
    """)
        # SELECT * FROM uczniowie WHERE imie = 'Anna' AND nazwisko = 'Ignaczuk'
        # % – dowolny ciąg znaków, dowolnek długości
        # SELECT COUNT (id) DROM UCZNIOWIE WHERE imie LIKE '%a' – lista osob ktorych imie konczy sie na litere a (lista dziewczyn)
        # SELECT imie, nazwisko, egz_mat FROM uczniowie WHERE egz_mat > 40 ORDER BY nawisko ASC
        # SELECT imie, nazwisko, egz_mat FROM uczniowie WHERE egz_mat > 40 ORDER BY egz_mat DESC LIMIT 5
        #        SELECT imie, nazwisko, klasa FROM uczniowie INNER JOIN klasy ON uczniowie.id_klasa=klasy.id WHERE klasa='1A' AND rok_naboru=2012
        # SELECT imie, nazwisko, klasa FROM uczniowie
        #  SELECT imie, nazwisko, klasa FROM uczniowie INNER JOIN klasy ON uczniowie.id=klasy.id WHERE klasy.id=(SELECT klasy.id FROM klasy WHERE klasa='1A' AND rok_naboru=2012  )

#        WITH srednie AS (
#           SELECT nazwisko, imie, AVG(ocena) AS sred FROM uczniowie
#            INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
#           GROUP BY uczniowie.id
#        ) SELECT nazwisko, imie, sred FROM srednie
#            WHERE sred > 3.5 ORDER BY sred DESC

        # 
        # 
        # 
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)


def main(args):
    # KONFIGURACJA ############
    
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    kwerenda(cur)
    
    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
