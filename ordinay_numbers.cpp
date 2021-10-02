
# include <iostream>
# include <vector>

using namespace std;

int check_if_ordinary(int digit, int num){
    int split;
    int count = 1;
    vector <int> numbers;
    numbers.clear();
    
    for (int k = 1; k <= num; k++){
        // checks if number is less than 10
        if (digit <= 9){
            return true;            
        }
        // if number is greater than 9
        else if (digit > 9){
            // cout << "digit is: " << digit << endl;
            for (int i = 10; i <= digit; i++){
                for (; digit > 0; digit /= 10){
                    split = digit % 10;
                    numbers.push_back(split);
                    for (int i = 0; i < numbers.size(); i++){
                        // cout << numbers[i] << " ";
                    }
                }
            }
        }
        // cout << "\nstarts to check" << endl;
        // checks if ele in numbers are equal
        int count = 1;
        for (int i = 0; i < numbers.size(); i++){
            // cout << "\n" << numbers[i];
            for (int j = i + 1; j < numbers.size(); j++){
                if (numbers[i] != numbers[j]){
                    // cout << numbers[i] << numbers[j] << endl; 
                    count = 0;
                    return false;
                    // cout << "count is: " << count << endl;
                }
            }
        }

        if (count == 1){
            return true;
        }
    }
    return false;
}

int main()
{
    int test_cases, num, split, check;
    // vector <int> numbers;
    vector <int> list_of_ordinary;
    cin >> test_cases;
    int z = 1;
    while (z <= test_cases){ 
        cin >> num;
        
        for (int i = 1; i <= num; i++){
            check = check_if_ordinary(i, num);
            if (check == true){
                // cout << "i is" << i << endl;
                list_of_ordinary.push_back(i);
            }
        
        }
        //  prints the size of list_of_ordinary numbers
        // cout << "the total numbers are: " << endl;
        cout << list_of_ordinary.size() << endl;
        // cout << "the digits are: " << endl;
        // for (int i = 1; i < list_of_ordinary.size(); i++){
            // cout << "\n" << list_of_ordinary[i] << endl;
        // }
        list_of_ordinary.clear();
        z += 1;
    }
    return 0;
}
