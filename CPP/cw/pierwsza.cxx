/*
 * pierwsza.cxx
 */


#include <iostream>
#include <cstdlib>
using namespace std;


bool czy_pierwsza(int n) 
{
    if(n<2)
        return false;
    for(int i=2; i*i<=n; i++)
        if(n%i==0)
            return false;
    return true
}

int main(int argc, char **argv)
{
    int n;
    
    cout<<"Podaj liczbę: ";
    cin>>n;
    
    if(czy_pierwsza(n))
        cout<<"Liczba "<<n<<"Jest pierwsza"<< endl;
    else
        cout<<"Liczba "<<n<<"Nie jest pierwsza"<< endl;
    
    system("pause");
    return 0;
}

