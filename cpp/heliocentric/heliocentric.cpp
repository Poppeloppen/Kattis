#include <iostream>
using namespace std;

int main()
{   
    int n = 1;
    int earth, mars;
    while(cin >> earth >> mars){ // run until end of input

        int days = 0;
        while (earth != 0 || mars != 0){
            earth++;
            mars++;
            days++;
            earth %= 365;
            mars %= 687;

        }
        cout << "Case " << n << ": " << days << endl;
        
        n++;
    }

    return 0;
}

