# include <iostream>
# include <vector>
# include <algorithm>
# include <numeric>

using namespace std;

// void print_lcm(unsigned long num1, unsigned long num2){
//     unsigned long gcd = __gcd(num1, num2);
//     unsigned long lcm = ((num1 * num2) / gcd) ;
//     cout << lcm << endl;
// }


int main()
{
    int test_cases;
    unsigned long l, r;
    cin >> test_cases;
    for (int i = 0; i < test_cases; i++){
        cin >> l >> r ;
        if (l* 2 > r){
            cout << -1 << " " << -1 << endl;
        }
        else{
            cout << l << " " << 2 * l << endl; 
        }
    }
    return 0;
}

// void print_vector(std::vector<int> const & elements) {
//     for(auto e : elements) {
//         std::cout << e << " ";
//     }
// }
