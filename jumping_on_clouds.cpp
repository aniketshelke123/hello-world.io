# include <bits/stdc++.h>
# include <iostream>
# include <math.h>
# include <vector>
# include <string>
# include <algorithm>
# define lli long long int
# define li long int
# define ld long double
using namespace std;

void take_input_in_vector(int numbers, vector <int> & elements){
    int input;
    for (int i = 0; i < numbers; i++){
        cin >> input;
        elements.push_back(input);
    }
}
void print_answer_vector(vector <int> const & answer){
    for (auto e: answer){
        cout << e << " ";
    }
    cout << endl;
}

int jumping_on_clouds(vector <int> const & elements, int n, int k){
    int next_cloud_index = 0;
    int thunder = 0;
    int jump = 0;
    int energy = 100;
    while (true){
        int next_cloud_index = (next_cloud_index + k) % n;
        int next_cloud = elements[next_cloud_index];
        jump++;
        if (next_cloud == 1){
            thunder++;
        }
        if (next_cloud_index == 0){
            break;
        }
    }
    // cout << "jump and thunder: "<< jump << " " << thunder << endl;
    energy = 100 - (jump + 2 * thunder);
    return energy;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k, jump = 0, thnder = 0, index = 0;
    vector <int> elements;
    cin >> n >> k;
    take_input_in_vector(n, elements);    
    cout << jumping_on_clouds(elements, n, k);
    return 0;
}
