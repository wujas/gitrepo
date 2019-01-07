/*
 * cw_sss.cpp
 */


#include <iostream>
using namespace std;


void cw1(){
     int suma = 0;

    for(int i = 10; i <= 99; i++)
    {
           if ( i % 2 == 0 ) suma=suma+i;         
    }
    
    cout << "Suma wszystkich parzystych liczb dwucyfrowych to: " << suma;
}

void cw2() {
    int a;
    int b;
    int c;
    cin >> a;
    cin >> b;
    cin >> c;
    while(a+b!=c) {
    a = b;
    b = c;
    cin >> c;    
    }
    cout << c;    
}

int main(int argc, char **argv)
{

    //~cout << "Suma wszystkich parzystych liczb dwucyfrowych to: " << cw1() << endl;
    cw1();
    cout << " " << endl;
    cw2();
    return 0;
}
