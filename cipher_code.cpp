# include <bits/stdc++.h>
# include <iostream>
# include <math.h>
# include <vector>
# include <string>
# include <algorithm>
# define lli long long int
# define li long int
# define ld long double
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int num;
    string st;
    getline(cin, st);
    cin >> num;
    
    for (int i = 0; st[i] != '\0'; i++)
        if (st[i] != 32)
            cout << char(int(st[i]) + num); 
        else{
            cout << " ";
        }
    return 0;
}
