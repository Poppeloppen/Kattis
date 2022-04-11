#include <iostream>
using namespace std;

int main()
{
    int g, t, n;
    cin >> g >> t >> n;
    
    double res = 0.9*(g - t);
    
    int total_item_weight = 0;
    for (int i = 0; i<n; i++){
        int item;
        cin >> item;

        total_item_weight += item;
    }   
    
    cout << res-total_item_weight << endl;
    


    return 0;
}
