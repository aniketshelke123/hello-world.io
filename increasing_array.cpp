
# include <iostream>
# include <vector>

using namespace std;

void take_input_in_vector(long long numbers, vector <long long> & elements){
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

int main()
{

    long long size_of_array;
    vector <long long> element;
    long long moves = 0, diff = 0;

    cin >> size_of_array;
    take_input_in_vector(size_of_array, element);

    for (int i = 0; i < size_of_array - 1; i++){
        diff = 0;
        if (element[i + 1] < element[i]){
            diff = element[i] - element[i + 1];
            moves += diff;
            element[i + 1] = element[i];
        }
    }
    // print_answer_vector(element);
    cout << moves << endl;

    return 0;
}
