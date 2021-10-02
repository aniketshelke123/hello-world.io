 
# include <iostream>
# include <vector>

using namespace std;


int main()
{
    string st;
    cin >> st;
    // cout << st;
    int count  = 1;
    int maximum = 1;
  
    int len = st.length();
    if (len > 1){
        for (int i = 1; i < len; i++){
            if (st[i - 1] == st[i]){
                count++;
                if (count > maximum){
                    maximum = count;
                }
            }
            else{
                count = 1;
            }
        }
    }
    cout << maximum << endl;
    return 0;
}