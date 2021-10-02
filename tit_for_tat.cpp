// https://codeforces.com/problemset/problem/1516/A

# include <iostream>
# include <vector>

using namespace std;

int main()
{
    long long input;
    long long test_cases, no_of_vector_elements, k;
    vector <int> elements;
    cin >> test_cases;
    while (test_cases --){
        cin >> no_of_vector_elements >> k;

        // taking Input in vector elements
        for (int i = 0; i < no_of_vector_elements; i++){
            cin >> input;
            elements.push_back(input);
        }

        while (k--){
            // Sub and add 1 for first two numbers in array
            long long counter = 0;
            for (int i = 0; i < elements.size(); i++){
               //  if (elements[i] != 0){
               //      counter += 1;
               //  }

                // subtracts 1 from first non-negative/zero element in vector
               // if (counter == 1){
            
               if (elements[i] > 0){
                  elements[i]--;
                  break;
               }
               // if (elements.back() >= 0){
                  // elements[elements.size() - 1]++;
                  // break;
               // }
            }
            // if (elements.back() >= 0){
            elements[elements.size() - 1]++;
               // break;
            // }

            // adds 1 to last element in vector
            // int var;
            // if (elements.back() >= 0){
            //     var = elements.back();
            //    //  cout << var << endl;
            //     elements.pop_back();
            //     elements.push_back(var + 1);
            //     // break;
            // }
        
        } //while ends
        // code for printing vector_elements
        for (int i = 0; i <elements.size(); i++){
            cout << elements[i] << " ";
        }
        cout << endl;
        elements.clear();
    }
    return 0;
}