/*
 * silnia.cpp
 */


#include <iostream>
using namespace std;

int silnia_it(int a){
    int wynik = 1;
    
    for(int i = 1; i <= a; i++){
        wynik = wynik * i; 
        
    }
    return wynik;
}

int silnia_re(int a)
{
    if (a == 0) return 1;  
    return silnia_re(a-1) * a;  
}

int main(int argc, char **argv)
{
    int a;
    cout << "Podaj liczbę ";
    cin >> a;
    cout << "Silnia: " << silnia_it(a) << endl;
    cout << "Silnia: " << silnia_re(a) << endl;
    return 0;
}

