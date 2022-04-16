#include <iostream>
#include <string>
using namespace std;

int main()
{
    string inp;
    cin >> inp;
    int len_inp = inp.size();
    int counter = 0;
    for (int i = 0; i < len_inp; i++){
        if (i % 3 == 0 && inp[i] != 'P'){
            counter++;
        } else if (i % 3 == 1 && inp[i] != 'E') {
            counter++;
        } else if (i % 3 == 2 && inp[i] != 'R') {
            counter++;
        }
    }
    cout << counter << endl;
    return 0;
}
