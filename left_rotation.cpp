# include <bits/stdc++.h>
# include <iostream>
# include <vector>
# include <algorithm>
# include <numeric>
# include <string>
# include <ctype.h>
# define lli long long int
# define li long int
#define ld long double
using namespace std;

void take_input_in_vector(vector <int> & vec1, int n){
	int input;
	for (int i = 0; i < n; i++){
		cin >> input;
		vec1.push_back(input);
	}
}

void print_vector(vector <int> const & answer){
	for (auto e: answer){
		cout << e << " ";
	}
}

void rotate_left(int d, int n, vector <int> & vec1, vector <int> & vec2){
	int temp = 0;
	for (int i = 0; i < vec1.size(); i++){
		temp = vec1[(i + d) % n];
		vec2.push_back(temp);
	}
	print_vector(vec2);
}

		
int main(){
	int n, no_of_left_rotation;
	cin >> n >> no_of_left_rotation;
	
	vector <int> vec1, vec2;
	take_input_in_vector(vec1, n);
	// print_vector(vec1);
	rotate_left(no_of_left_rotation, n, vec1, vec2);
		
	return 0;
}

