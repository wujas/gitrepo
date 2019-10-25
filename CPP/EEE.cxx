/*
 * EEE.cxx

 */

using namespace std;

#include <iostream>
#define MAKS 50

int main(int argc, char **argv)
{

    char imie[MAKS];
    char nazwisko[MAKS];


    cout << "Podaj imię: " << endl;
    cin.getline(imie, MAKS);
    cout << "Podaj nazwisko: " << endl;
    cin.getline(nazwisko, MAKS);
    cout << "Witaj " << imie << " " <<nazwisko;
    
    return 0;
}

