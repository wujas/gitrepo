/*
 * nieparzyste.cpp
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int n;
    cout << "Podaj liczbę: ";
    cin >> n;
    
    for(int i = 1; i <= n; i++){
        if((i %2) != 0)
            i++;
        cout << i;
        
        
    }
    return 0;
}

