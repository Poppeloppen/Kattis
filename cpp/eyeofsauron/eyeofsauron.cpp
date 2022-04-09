#include <iostream>
#include <string>
using namespace std;

int main()
{
    string inp;
    cin >> inp;

    int idx = (inp.size() / 2)-1;
    char c = inp[idx];

    if (inp.size() % 2 == 0 && inp[idx] == '('){
        cout << "correct" << endl;
    } else {
        cout << "fix" << endl;
    }
    return 0;
}


