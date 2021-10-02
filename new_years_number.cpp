# include <iostream>
# include <vector>

using namespace std;

void chech_no_of_years(){
    long long no_of_years;
    cin >> no_of_years;
    long long x = 0;
    long long y = 0;
    long long i = 0;
    while (i < 1000){
        long long j = 0;
        while(j < 1000){
            if (2020 * i + 2021 * j == no_of_years){
                x = i;
                y = j;
                break;
            }
            j += 1;               
        }
        i += 1;
    }         
    if (x != 0 || y != 0){
        cout << "YES" << endl;
    }
    else if (x == 0 && y == 0){
        cout << "NO" << endl;
    }
}

int main()
{
    // int x, y;
    int test_cases;
    cin >> test_cases;

    while (test_cases--){
        chech_no_of_years();
    }
    return 0;
}
