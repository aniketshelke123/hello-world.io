
# include <iostream>
# include <vector>
# include <random>
# include <algorithm>

using namespace std;

void take_input_in_vector(int numbers, vector <int> & elements){
    int input;
    for (int i = 0; i < numbers; i++){
        cin >> input;
        elements.push_back(input);
    }
}

void print_vector(vector <int> & elements){
    for (int i = 0; i < elements.size(); i++){
        cout << elements[i] << " ";
    }
}

int funct_b(vector <int> & elements, int limit){
    int sum_of_weights = 0;
    int sum = accumulate(elements.begin(), elements.end(), 0);
    for (int num = 0; num < elements.size(); num++){
        sum_of_weights += elements[num];
        if (sum_of_weights > limit){
            return true;
        }
        else if (sum < limit){
            return true;
        }
       
        else if (sum_of_weights == limit){
            return false;
        }
    }
    return false;
}

int funct_c(vector <int> & elements, int limit){
    for (int i = 0; i < 10; i++){
        random_shuffle(elements.begin(), elements.end());
        int check = funct_b(elements, limit);
        // cout << check << endl;
        if (check){
            return true;
        }
    }
    return false;
}
int main()
{
    int test_cases, num_of_elements;
    vector <int> elements;
    int x;
    cin >> test_cases;
    while(test_cases--){
        cin >> num_of_elements >> x;
        take_input_in_vector(num_of_elements, elements);

        int sum = accumulate(elements.begin(), elements.end(), 0);
        int max = *max_element(elements.begin(), elements.end());
        for (int i = 0; i < elements.size(); i++){
            if (max > x){
                sort(elements.begin(), elements.end(), greater<int>());
                cout << "YES" << endl;
                print_vector(elements);
                cout << endl;
                break;
            }
            else if (sum == x){
                cout << "No" << endl;
                break;
            }
            else{ // 1 2 3 4  x =3
                if (elements[i] <= x){
                    int B = funct_b(elements, x);
                    if (B == true){
                        cout << "YES" << endl;
                        print_vector(elements);
                        cout << endl;
                        break;
                    }
                    if (B == false){
                        int C = funct_c(elements, x);
                    }
                }
                if (elements[i] == x){
                    int Z = funct_c(elements, x);
                    if (Z){
                        print_vector(elements);
                    }
                }
            }
        }
        elements.clear();
    }
    return 0;
}

