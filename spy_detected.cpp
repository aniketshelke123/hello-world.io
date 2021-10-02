// https://codeforces.com/problemset/problem/1512/A

# include <iostream>
# include <vector>

using namespace std;

void take_input_in_vector(int numbers, vector <int> & elements){
    int input;
    for (int i = 0; i < numbers; i++){
        cin >> input;
        elements.push_back(input);
    }
}
void print_vector(vector <int> const & elements){
    for (auto e: elements){
        cout << e << " ";
    }
    cout << endl;
}

int main()
{
    int test_cases,num_of_elements, equal_num;
    vector <int> elements;
    cin >> test_cases;
    while (test_cases--){
        cin >> num_of_elements;
        take_input_in_vector(num_of_elements, elements);

        for (int i = 0; i < elements.size(); i++){
            if (elements[i] == elements[i + 1]){
                equal_num = elements[i];
            }
        }
        // cout << "equal num is: " << endl;
        // cout << equal_num << endl;

        for (int i = 0; i < elements.size(); i++){
            if (elements[i] == equal_num){
                continue;
            }
            else{
                cout << i + 1 << endl;
            }
        }
        // print_vector(elements);
        elements.clear();
        equal_num = 0;
    }
    return 0;
}
