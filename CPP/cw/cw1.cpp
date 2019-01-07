/*
 * cw1.cpp
 */


#include <iostream>
using namespace std;

    
int main(int argc, char **argv)
{
     int suma = 0;

    for(int i = 10; i <= 99; i++)
    {
           if ( i % 2 == 0 ) suma=suma+i;         
    }
    
    cout << "Suma wszystkich parzystych liczb dwucyfrowych to: " << suma;
}


