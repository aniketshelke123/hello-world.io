
# include <iostream> 
# include <vector>
# include <algorithm>
# include <string>


using namespace std;

void take_input_in_vector(int numbers, vector <long long> & elements){
    for (int i = 1; i <= numbers; i++){
        elements.push_back(i);
    }
}
void copy_even_to_answer(vector <long long> const & even, vector <long long> & answer){
    for (int i = 0; i < even.size(); i++){
        answer.push_back(even[i]);
    }
    // cout << endl;
}

void copy_odd_to_answer(vector <long long> const & odd, vector <long long> & answer){
    for (int i = 0; i < odd.size(); i++){
        answer.push_back(odd[i]);
    }
    // cout << endl;
}

void vector_answer(vector <long long> const & answer){
    for (auto e: answer){
        cout << e << " ";
    }
    // cout << endl;
}

// void print_odd_vector(vector <long long> const & odd){
//     for (auto e: odd){
//         cout << e << " ";
//     }
//     cout << endl;
// }
void seperate_odd_even(long long num, vector <long long > & elements, vector <long long> & even, vector<long long> & odd){
    for (int i = 1; i <= num; i++){
        if (i % 2 == 0){
            even.push_back(i);
        }
        else{
            odd.push_back(i);
        }
    }
}

int main()
{
    long long num;
    vector<long long> elements, odd, even, answer;
    cin >> num;
    if (num > 1 && num < 4){
        cout << "NO SOLUTION"<< endl;
    }
    else{
        take_input_in_vector(num, elements);
        seperate_odd_even(num, elements, even, odd);
        copy_odd_to_answer(even, answer);
        copy_even_to_answer(odd, answer);
        vector_answer(answer);
    }

    return 0;
}
