# include <iostream>

using namespace std;

int main()
{
    long long num;
    cin >> num ;
    cout << num << endl;
    while (num != 1){
        if (num % 2 == 0){
            num = num / 2;
            cout << num << endl;
        }
        else{
            num = (num * 3) + 1;
            cout << num << endl;
        }
    }

    return 0;
}