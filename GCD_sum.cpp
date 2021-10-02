# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;

template <class T>

T sum_of_digits(T num){
    T sum = 0;
    while(num){
        int split = num % 10;
        sum += split;
        num /= 10;
    }
    return sum;
}

template <class T>
T checks_condition(T num){
    T digit_sum = sum_of_digits(num);
    T gcd = __gcd(num, digit_sum);
    return gcd
}

template <class T>
T answer(T num){
    T gcd = checks_condition(num);
    while (gcd <= 1){
        gcd = checks_condition(++num);
    }
    return num;
}

int main()
{
    int test_cases;
    long long num;
    cin >> test_cases;
    while (test_cases--){ 
        cin >> num;
        cout << answer(num) << endl;
    }
    return 0;
}   
