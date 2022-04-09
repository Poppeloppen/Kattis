#include <iostream>
using namespace std;


int main()
{
    double c, l;
    cin >> c >> l;
    
    double total_cost = 0.;
    for (int i = 0; i< l; i++){
        double wid, len;
        cin >> wid >> len;

        total_cost += wid * len * c;
    }
    cout.precision(10); // this line was added, as a more precise result were required to pass all the test cases 
    cout << total_cost << endl;
    
    return 0;
}

