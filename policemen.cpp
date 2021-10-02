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



void take_input_in_vector(long long numbers, vector <lli> & elements){
    int input;
    for (int i = 0; i < numbers; i++){
        cin >> input;
        elements.push_back(input);
    }
}

// void print_answer_vector(vector <long long> const & answer){
//     for (auto e: answer){
//         cout << e << " ";
//     }
//     cout << endl;
// }

int min_stars(lli size_of_array, vector <lli> & element){
    for (int i = 0; i < size_of_array - 1; i++){
        if (element[i + 1] <= element[i]){
            element[i + 1] = element[i] + 1;
        }
    }
    int sum_2 = accumulate(element.begin(), element.end(), 0);
    return sum_2;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    lli size_of_array;
    vector <lli> element;

    cin >> size_of_array;
    take_input_in_vector(size_of_array, element);
    sort(element.begin(), element.end());
    int sum_1 = accumulate(element.begin(), element.end(), 0);
    // print_answer_vector(element);
    int sum_2 = min_stars(size_of_array, element);
    // print_answer_vector(element);
    int no_of_stars = int(sum_2 - sum_1);
    cout << "The no. of stars are: " << no_of_stars;
    return 0;
}