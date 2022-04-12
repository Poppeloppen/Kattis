#include <iostream>
#include <cmath>
using namespace std;


int main()
{
    int n;
    cin >> n;
    
    double total_score = 0;
    double total_hits = 0;
    for (int i = 0; i < n; i++){
        int score;
        cin >> score;

        if (score >= 0){
            total_score += score;
            total_hits++;
        }
    }
    double res = total_score / total_hits;
    cout.precision(15);
    cout << res << endl;
    return 0;
}


