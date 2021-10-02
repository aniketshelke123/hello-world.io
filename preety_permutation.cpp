
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
    for (int i = 1; i <= numbers; i++){
        elements.push_back(i);
    }
}

void print_answer_vector(vector <int> const & vect_a){
    for (auto e: vect_a){
        cout << e << " ";
    }
    cout << endl;
}

void swap_even_n(int n, vector <int> & vect_a){
    if (n % 2 != 0){
        n = n - 1;
    }
    for (int i = 1; i <= n; i++){
        if (i % 2 != 0){
            vect_a.push_back(i + 1);
        }
        else{
            vect_a.push_back(i - 1);
        }
    }
}

void swap_last_two_elements(int n, vector <int> const & elements, vector <int> & vect_a){
    int last_ele_of_vect_a = vect_a[vect_a.size() - 1];
    int last_index_of_vect_a = last_ele_of_vect_a;

    replace(vect_a.begin(), vect_a.end(), last_ele_of_vect_a, elements[n - 1]);
    vect_a.push_back(last_ele_of_vect_a);

}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector <int> elements, vect_a,vect_answer;
    int n, test_cases;
    cin >> test_cases;

    while (test_cases--)
    {
        cin >> n;
        take_input_in_vector(n, elements);
        if (n % 2 == 0){
            swap_even_n(n, vect_a);
            print_answer_vector(vect_a);
        }
        else{
            swap_even_n(n , vect_a);
            swap_last_two_elements(n, elements, vect_a);
            print_answer_vector(vect_a);
        }
        vect_a.clear();
        elements.clear();
    }
    

    return 0;
}