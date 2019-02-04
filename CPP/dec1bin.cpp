/*
 * dec2bin.cpp
 * 

 */

#include <iostream>
#include <cmath>
using namespace std;



int dec2any(int liczba, int podstawa, int tab[]) {
    int i = 0;
    do {
        tab[i] = liczba % podstawa;
        liczba = liczba / podstawa;
        i++;
        } while(liczba != 0);
        return i-1;
    }

//~n = 3
//~711(n) = 7*(n-1)^2+1*(n-2)^1+1*(n-3)^0

int any2dec(int tab[]) {
    int podstawa = 0;
    do {
        cout << "Podstawa <2;9>: ";
        cin >> podstawa; 
    } while(podstawa < 2 || podstawa > 9);
    
    int ile = 0;
    cout << "Ile cyfr? "; cin >> ile;
    for(int i = 0; i < ile; i++)
        do{
            cout << "Podaj cyfrę (0-" << podstawa-1 << "): ";
            cin >> tab[i];
        } while (tab[i]<0 || tab[i]>podstawa-1);
    // konwersja na system dziesiętny
    for (int i = 0; i < ile; i++) {
    // kolejna liczba z tabeli mnożona przez odpowiednią potęgę podstawy
        
        
        }
    }

int main(int argc, char **argv)
{
    int tab[8];
    int liczba, podstawa;
	cout << "Podaj liczbę i podstawę systemu docelowego: ";
    cin >> liczba >> podstawa;
    int i = dec2any(liczba, podstawa, tab);
    cout << "Wynik: ";
    while (i >= 0) {
        cout << tab[i];
        i--;
    }
    
    
	return 0;
}
