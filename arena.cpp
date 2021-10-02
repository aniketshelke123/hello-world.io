
# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;

void take_input_in_vector(int numbers, vector <int> & elements){
    int input;
    for (int i = 0; i < numbers; i++){
        cin >> input;
        elements.push_back(input);
    }
}

int main()
{
    int test_cases;
    int no_of_elements;
    vector <int> elements;
    cin >> test_cases;
    while (test_cases--){
        cin >> no_of_elements;
        
        take_input_in_vector(no_of_elements, elements);

        auto min_itr = min_element(elements.begin(), elements.end());
        int min_num = *min_itr;
        // cout << min_num << endl;
        // elements.erase(min_itr);
        int count_of_smallest = count(elements.begin(), elements.end(), min_num);
        // cout << count_of_smallest << endl;
        // elements.erase(elements.begin() + count_of_smallest);
        // if (count(elements.begin(), elements.end(), min_num) > 1){
            // cout << "YEs" << endl;
        // }
        for (int i = 0; i < count_of_smallest; i++){
            elements.erase(min_itr);
        }
        // cout << "answer" << endl;
        cout << elements.size() << endl;
        elements.clear();
    }
    return 0;
}

