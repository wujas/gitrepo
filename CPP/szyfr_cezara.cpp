/*
 * szyfr_cezara.cpp
 */


#include <iostream>
using namespace std;

#define MAKS 100

void szyfruj(char tekst[], int klucz){
    int kod = 0;
    for(int i = 0; i < MAKS; i++) {
        kod = (int)tb[i];
        if (kod > 96 &7)
    }
}



int main(int argc, char **argv)
{
    char tekst[MAKS];
    int klucz = 0;
    cout << "Podaj tekst: ";
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    cout << "Szyfr cezara do tekstu: " << endl;
    szyfruj(tekst, MAKS);
    return 0;
}

