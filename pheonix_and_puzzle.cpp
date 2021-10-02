
# include <iostream>
# include <vector>
# include <algorithm>
# include <math.h>

using namespace std;

// cout << sqrt(12) << endl;
int main()
{
    int test_cases;
    long long element;
    cin >> test_cases;
    while (test_cases--){
        cin >> element;
        
        cout << int(sqrt(12)) << endl;
        if (2 * sqrt(element) == element || 4 * sqrt(element) == element){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }


    }
    return 0;
}