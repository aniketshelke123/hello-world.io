
# include <iostream>
# include <vector>
using namespace std;

int main()
{
    int cash;
    vector<int>  denomination {100,20,10,5,1}; //  int denomination[] = {100, 20, 10, 5, 1};
    int len_of_deno = denomination.size();
    int count = 0;

    // cout << "Enter the cash: ";
    cin >> cash;
    
    for (int i = 0; i < len_of_deno; i++) {
        while (cash >= denomination[i]) 
        {
            cash -= denomination[i];
            count += 1;
            //cout << cash << endl;
        }
    }
    cout << count;
    return 0;
}
