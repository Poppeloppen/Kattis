#include <iostream>
using namespace std;

int main()
{
    int x, n;
    cin >> x >> n;
    
    int total = 0;
    for (int i = 0; i < n; i++){
        int used_data;
        cin >> used_data;
        total += used_data;
            }
    cout << (n+1) * x - total << endl;

    return 0;
}

