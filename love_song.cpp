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

void push_str_into_vector(vector <li> & vect_str, string str, li num){
    for (li i = 0; i < num; i++){
        vect_str.push_back(str[i]);
    }
}

void print_vector(vector <li> const & answer){
    for (auto e: answer){
        cout << e << endl;
    }
}

void length_of_string(vector <li> const & vect_str, vector <li> & answer){
    li count = 0;
    int l = 0, r = 0;       // l and r is the range of the question
    cin >> l >> r;
    for (lli i = l - 1; i <= r - 1; i++){
        int character = vect_str[i] - 96;
        count += character;
    }
    answer.push_back(count);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    li num, question;
    string str;
    vector <li> vect_str;
    vector <li> answer;
    cin >> num >> question;
    cin >> str;

    push_str_into_vector(vect_str, str, num);
    while(question--){
        length_of_string(vect_str, answer); 
    }
    print_vector(answer);
    return 0;
}