
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


void take_input_in_vector(int numbers, vector <int> & elements){
    int input;
    for (int i = 0; i < numbers; i++){
        cin >> input;
        elements.push_back(input);
    }
}


void print_answer_vector(vector <int> const & answer){
    for (auto e: answer){
        cout << e << " ";
    }
    cout << endl;
}

void changing_the_vect(vector <int> & vect_a, vector <int> const & vect_b , int n, vector<int> & vect_x, vector <int> & vect_y){
    for(int i = 0; i < n; i++){
        int diff = 0, p = 0;
        if (vect_a[i] > vect_b[i]){
            p = i;
            diff = vect_a[i] - vect_b[i];
            vect_a[i] = vect_a[i] - diff;
        }
        for (int i = 1; i <= diff; i++){
            vect_x.push_back(p + 1);
        }
    }
    for(int i = 0; i < n; i++){
        int diff = 0, p = 0;
        if (vect_a[i] < vect_b[i]){
            p = i;
            diff = vect_b[i] - vect_a[i];
            vect_a[i] = vect_a[i] + diff;
        }
        for (int i = 1; i <= diff; i++){
            vect_y.push_back(p + 1);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector <int> vect_a, vect_b, vect_x, vect_y;
    int test_cases, n;
    cin >> test_cases;

    while (test_cases--){
        cin >> n;
        take_input_in_vector(n, vect_a);
        take_input_in_vector(n, vect_b); 

        if (accumulate(vect_a.begin(), vect_a.end(), 0) != accumulate(vect_b.begin(), vect_b.end(), 0)){
            cout << -1 << endl;
        }
        else{
            changing_the_vect(vect_a, vect_b, n, vect_x, vect_y);
            cout << vect_x.size() << endl;
            if (vect_x.size() > 0){
                for (int i = 0; i < vect_x.size(); i++){
                    cout << vect_x[i] << " " << vect_y[i] << endl;
                }
            }
        }

        vect_a.clear();
        vect_b.clear();
        vect_x.clear();
        vect_y.clear();
    
    }
    return 0;
}
