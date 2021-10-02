// not completed
# include <iostream>
# include <vector>
# include <math.h>
# include <numeric>
# include <algorithm>
using namespace std;

void take_input_in_vector(int numbers, vector <long long> & elements){
    int input;
    for (int i = 0; i < numbers; i++){
        cin >> input;
        elements.push_back(input);
    }
}

// void print_vector(vector <long long> const & elements){
//     for (auto e: elements){
//         cout << e << " ";
//     }
//     cout << endl;
// }


int main()
{
    int test_cases;
    int no_of_elements;
    // int sum_of_numbers = 0;
    vector <long long> elements;
    cin >> test_cases;
    while (test_cases--){
        int sum_of_numbers = 0;
        long long sum_of_vector_elements = 0;
        cin >> no_of_elements;

        take_input_in_vector(no_of_elements, elements);
        sum_of_vector_elements = accumulate(elements.begin(), elements.end(), 0ll);
        // cout << "sum of vector elements: " << sum_of_vector_elements << endl;

        for (int i = 0; i < no_of_elements; i++){
            sum_of_numbers += i;
        }
        // cout << "sum of numbers: " << sum_of_numbers << endl;

        if (sum_of_numbers < sum_of_vector_elements){
            for (size_t i = 0; i < elements.size(); i++)
            {
                if (elements[i] == 0 && elements[i + 1] == 0){
                    cout << "NO" << endl;
                    break;
                }
                else{
                    cout << "YES" << endl;
                    break;
                }
            }
        }
        else{
            for (int i = 0; i < elements.size(); i++){
                if (count(elements.begin(), elements.end(), elements[i]) > 1){
                    cout << "NO" << endl;
                    break;
                }
                else{
                    cout << "yes" << endl;
                    break;
                }
            }
        }
        elements.clear();

    }
    return 0;
}
