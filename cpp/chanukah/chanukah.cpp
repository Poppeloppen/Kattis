#include <iostream>
using namespace std;


int main()
{
    int p;
    cin >> p;

    for (int i = 0; i<p; i++){
        int k, n;
        cin >> k >> n;

        int res;
        res = (n*(n+1))/2;

        cout << k << ' ' <<  res+n << endl;
        }

    return 0;
}
