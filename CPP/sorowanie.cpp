/*
 * sorowanie.cpp
 * 
 * 
 */


#include <iostream>
#include <cstdlib>
using namespace std;


void wypelnij(int tab[], int roz){
    srand(time(NULL));  // inicjacja generatora liczb pseudo losowych
    for(int i=0; i < roz; i++) {
        //~cout << rand() << endl;
        tab[i] = rand() % 101;

    }
}

void drukuj(int tab[], int roz){
    for(int i=0; i < roz; i++) {
        cout << tab[i] << " " ;

    }
    cout << endl;
}

void zamien1(int &a, int &b){
    //~cout << a << " " << b << endl;
    int tmp = a;
    a = b;
    b = tmp;
    //~cout << a << " " << b << endl;
    
}    

void zamien2(int &a, int &b){
    //~cout << a << " " << b << endl;
    int tmp = a;
    a = b;
    b = tmp;
    //~cout << a << " " << b << endl;
    
}    
    
    
    
void sort_bubble(int tab[], int n) {
    for (int j = n - 1; j > 0; j--) {
        for(int i = 0; i < j; i++) {
            if (tab[i] > tab[i+1])
                zamien1(tab[i], tab[i + 1]);
        }
    }
}

void sort_bubbl2(int tab[], int n) {
    for (int j = n - 1; j > 0; j--) {
        for(int i = 0; i < j; i++) {
            if (tab[i] < tab[i+1])
                zamien1(tab[i], tab[i + 1]);
        }
    }
}

sort_insert

int main(int argc, char **argv)
{
    int roz = 20;
    int tab[roz];
    wypelnij(tab, roz);
    drukuj(tab, roz);
    cout << endl;
    //~tab[0] = 7;
    //~tab[1] = 5;
    //~zamien1(tab[0], tab[1]);
    //~cout << tab[0] << " " << tab[1];
    sort_bubble(tab, roz);
    drukuj(tab, roz);
    cout << endl;
    sort_bubbl2(tab, roz);
    drukuj(tab, roz);
    
    return 0;
}

