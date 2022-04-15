#include <iostream>
#include <string>
using namespace std;


int main(){
    int n;
    cin >> n;

    for (int i=0; i<n; i++){
        string str1;
        string str2;
        cin >> str1 >> str2;

        cout << str1 << endl;
        cout << str2 << endl;
        int length = str1.size();
        for (int j=0; j<length; j++){

            if (str1[j] == str2[j]){
                cout << '.';
            } else {
                cout << '*';
            }
        }
        cout << '\n' << endl;

    }
    return 0;
}
