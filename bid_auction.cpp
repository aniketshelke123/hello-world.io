
# include<iostream>
# include <vector>
# include <algorithm>
#include <bits/stdc++.h>
using namespace std;

// takes input into vector elements
void take_input_in_vector(long long numbers, vector <long long> & elements, vector <long long> & sorted_elements){
    long long input;
    for (int i = 0; i < numbers; i++){
        cin >> input;
        elements.push_back(input);
    }
}


// copy's the vec.elements to sorted_elements (vector) in ascending order
void copy_elements_to_sorted_elements(vector <long long> elements, vector <long long> & sorted_elements){
    // for (int i = 0; i < elements.size(); i++){
        // sorted_elements.push_back(elements[i]);
    // }
    sorted_elements = elements;
    sort(sorted_elements.begin(), sorted_elements.end());
}


long long checks_for_smallest_unique_number(vector <long long> & sorted_elements){
    int smallest_and_unique_number = false;
    
    // checks for the smallest unique number in the sorted_elements vector
    for(long long num = 0; num < sorted_elements.size(); num++){
        if (sorted_elements.size() == 1){
            smallest_and_unique_number = sorted_elements[num];
            return smallest_and_unique_number;
        }
    
        if (count(sorted_elements.begin(), sorted_elements.end(), sorted_elements[num]) == 1){
            smallest_and_unique_number = sorted_elements[num];
            return smallest_and_unique_number;
        }
    }
    return false;
}

void answer(vector <long long> & elements, vector <long long> & sorted_elements){
    int flag = checks_for_smallest_unique_number(sorted_elements);
    // cout << "flag: " << flag << endl;
    if (flag){
        auto it = find(elements.begin(), elements.end(), flag);
        // If element was found
        if (it != elements.end())
        {
            int index = it - elements.begin();
            cout << index + 1 << endl;
        }
    }
    else{
        cout << -1 << endl;
    }
    elements.clear();
    sorted_elements.clear();
}


int main()
{
    // Initialization
    int test_cases;
    long long  no_of_elements, smallest_and_unique_number;
    vector <long long> elements;
    vector <long long> sorted_elements;

    // takes input
    cin >> test_cases;
    while (test_cases--){
        cin >> no_of_elements;

        // takes input into the vector(elements)
        take_input_in_vector(no_of_elements, elements, sorted_elements);
        copy_elements_to_sorted_elements(elements, sorted_elements);
        
        // prints answer
        answer(elements, sorted_elements);
       
    }
    return 0;
}












// v.begin() returns the memory address of the first char
// e.g. 0x234235
// std::find returns the memory address of the found char, let's say it's at index 3, so (0x234235+3) so it returns 0x234238
// well now you have 0x234235 and 0x234238 but not 3, which is what you actually want
// so 0x234238 - 0x234235 = 3
// except that's garbage to look at
// so instead it's v.begin() - std::find(v.begin(),v.end(),mycharvalue);
// or whatever K is an abbreviation for
// or, even better
// no math at all
// std::distance(v.begin(), std::find(v.begin(), v.end(), K));
// because subtracting memory address by hand, even if they're cleverly hidden behind names, is kind of gross
// and easy to get wrong.
