
# include <iostream>
# include <vector>
# include <algorithm>
#include<bits/stdc++.h>

using namespace std;

void take_input_in_vector(int numbers, vector <long long> & elements){
    int input;
    for (int i = 0; i < numbers * 2; i++){
        cin >> input;
        elements.push_back(input);
    }
}

void print_answer_vector(vector <long long> const & answer){
    for (auto e: answer){
        cout << e << " ";
    }
    cout << endl;
}

void prints_answer(vector <long long> & elements, vector <long long> & answer){
    for (size_t long long i = 0; i < elements.size(); i++){
        while (elements.size() > 0){
            // pops min from elements and insert it into answer
            auto min_iter = min_element(elements.begin(), elements.end());
            int min_num = *min_iter;
            answer.push_back(min_num);
            elements.erase(min_iter);
            
            // pops max from elements and appends it to answer
            auto max_iter = max_element(elements.begin(), elements.end());
            int max_num = *max_iter;
            answer.push_back(max_num);
            elements.erase(max_iter);
        }
    }    
    print_answer_vector(answer);
    answer.clear();
}

int main()
{
    int test_cases;
    int num_of_elements;
    vector <long long> elements, answer;
    cin >> test_cases;
    while (test_cases--){
        cin >> num_of_elements;
        take_input_in_vector(num_of_elements, elements);
    
        prints_answer(elements, answer);
    }

}