
# include <iostream> 
# include <vector>
# include <algorithm>

using namespace std;


void take_input_in_vector(int numbers, vector <long long> & elements){
    int input;
    for (int i = 0; i < numbers - 1; i++){
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
    long long num;
    vector <long long> ele;
    cin >> num;
    take_input_in_vector(num, ele);
    sort(ele.begin(), ele.end());
    for (int i = 1; i <= num; i++){
        if (i != (ele[i - 1])){
            cout << i << endl;
            break;
        }
    }
    return 0;
}