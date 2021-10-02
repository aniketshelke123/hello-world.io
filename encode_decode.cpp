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

int push_str_into_vector_str1(string str1, vector <int> & vect_str1){
    int flag = 0;
    for (int i = 0; i < str1.size(); i++){
        if (str1[i] >= 48 && str1[i] <= 57){
            flag = 1;
        }
        else if (str1[i] >= 97 && str1[i] <= 122 || str1[i] >= 65 && str1[i] <= 90){
            vect_str1.push_back(str1[i] + 5);
        }
        else if (str1[i] == 44 || str1[i] == 46 || str1[i] == 32){
            vect_str1.push_back(str1[i]);
        }
    }
    if (flag == 0){
        return 1;
    }
    else{
        return 0;
    }
}

int push_str_into_vector_str2(string str2, vector <int> & vect_str2){
    int flag = 0;
    for (int i = 0; i < str2.size(); i++){
        if (str2[i] >= 48 && str2[i] <= 57){
            flag = 1;
        }
        else if (str2[i] >= 97 && str2[i] <= 122 || str2[i] >= 65 && str2[i] <= 90){
            vect_str2.push_back(str2[i] - 5);
        }
        else if (str2[i] == 44 || str2[i] == 46 || str2[i] == 32){
            vect_str2.push_back(str2[i]);
        }
    }
    if (flag == 0){
        return 1;
    }
    else{
        return 0;
    }
}
    
void print_vector(vector <int> const & answer){
    for (auto e: answer){
        cout << (char)e << "";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string st1, st2;
    getline(cin, st1);
    getline(cin, st2);
    vector <int> vect_str1, vect_str2;
    

    int a = push_str_into_vector_str1(st1, vect_str1);
    if (a == 0){
        cout << "INVALID INPUT";
    }
    else{
        print_vector(vect_str1);
    }
    cout << "\n";
    int b = push_str_into_vector_str2(st2, vect_str2);
    
    if (a != 0){
        if (b == 0){
            cout << "INVALID INPUT";
        }
    
        else{
            print_vector(vect_str2);
        }
    }
    return 0;
}
