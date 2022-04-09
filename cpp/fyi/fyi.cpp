#include <iostream>
using namespace std;


int main()
{
    int x;
    cin >> x;

    int first3 = x/10000;
    if (first3==555){
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }

    return 0;
}
