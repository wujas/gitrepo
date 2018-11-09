/*
 * anagram.cpp
 */


#include <iostream>
using namespace std;


int main(int argc, char **argv)
{
    char wyraz[] = "ryba";
    int r = 4;
    int i1, i2, i3, i4;
    i1 = i2 = i3 = i4 = 0;
    for(i1 = 0; i1 < r; i1++) {
        for(i2 = 0; i2 < r; i2++) {
            if (i1 == i2) continue;
                for(i3 = 0; i3 < r; i3++){
                    for(i4 = 0; i4 < r; i4++){
                        if (i3 == i4) continue;
                            cout << i1 << i2 << i3 << i4 << endl;
                    }
                }
            // cout << i1 << i2 << endl;
        }
    }
    return 0;
}

