# include <iostream>
# include <vector>
# include <bits/stdc++.h>
# include <iostream>
# include <math.h>
# include <string>
# include <algorithm>
# define lli long long int
# define li long int
using namespace std;


void take_input_in_vector(vector <string> & vec, int size){
	string input;
	for (int i = 0; i < size; i++){
		cin >> input;
		vec.push_back(input);
	}
}

void print_vector(vector <int> const & answer){
	for (auto e: answer){
		cout << e << "\n";
	}
}
void print_string_vector(vector <string> const & answer){
	for (auto e: answer){
		cout << e << " ";
}
}

void counting_the_string(vector <int> & answer, vector <string> & queries, vector <string> & str){
	for (int i = 0; i < queries.size(); ++i){
		int count = 0;
		string temp = queries[i];
		for (int j = 0; j < str.size(); ++j){
			if (temp == str[j]){
				count += 1;
			}
		}
		answer.push_back(count);
	}
	print_vector(answer);
}
		

int main(){

    	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n, q, input;
	vector<string> str, queries;
	vector <int> answer;
	
	cin >> n;
	take_input_in_vector(str, n);

	cin >> q;
	take_input_in_vector(queries, q);
	// print_string_vector(str);
	// print_string_vector(queries);
	counting_the_string(answer, queries, str);
	return 0;
}
