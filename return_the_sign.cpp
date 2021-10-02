# include <bits/stdc++.h>
# include <iostream>
# include <math.h>
# include <vector>
# include <string>
# include <numeric>
# include <ctype.h>
# include <algorithm>
# define lli long long int
# define li long int
# define ld long double

using namespace std;

void take_input_in_vector(int numbers, vector <int> & elements){
    int input;
    for (int i = 0; i < numbers; i++){
        cin >> input;
        elements.push_back(input);
    }
}

int check_for_sign(vector <int> const & elements){
    int multi = 1;
    int e = 0;
    for (const auto& e:elements){
        multi *= e;
    }
    if (multi == 0){
        return 0;
    }
    else if (signbit(multi) == 1){
        return -1;
    } 
    else{
        return 1;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    vector <int> elements;
    cin >> n;
    take_input_in_vector(n, elements);
    cout << check_for_sign(elements) << "\n";
    return 0;
}