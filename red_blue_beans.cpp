
# include <iostream>


using namespace std;

int main()
{
    long long int test_cases, red_beans, blue_beans, difference;

    cin >> test_cases;
    while (test_cases--){
        cin >> red_beans >> blue_beans >> difference;
        long minimum = min(red_beans, blue_beans);
        long maximum = max(red_beans, blue_beans); 

        // min(red, blue) * (d + 1) >= max(red, blue)...........
        // or b - r > r * d then no else yes where b is always max()...
        // if (minimum * (difference + 1) >= maximum){
                // cout << "YES" << endl;
            // }
        if (maximum - minimum <= difference * minimum){
            cout << "yes" << endl;
        }
        else{
            cout << "NO" << endl;
            }
    }
    return 0;
}