
# include <iostream>
# include <vector>

using namespace std;

int main()
{
    int test_cases, n, input;
    vector <int> odd, even;
    cin >> test_cases;
    int k = 1;
    while (k <= test_cases){
    cin >> n;

    for (int i = 0; i < n; i++){
        cin >> input;
        if (input % 2 == 0){
            even.push_back(input);
        }
        else if (input % 2 != 0){
            odd.push_back(input);
        }
        
    } 

    for (int i = 0; i < odd.size(); i++){
        cout << odd[i] << " ";
    }
    
    for (int i = 0; i < even.size(); i++){
        cout << even[i] << " ";
        
    }
    cout << endl;
    odd.clear();
    even.clear();
    k += 1;
    }
    return 0;
}
