# include <bits/stdc++.h>
# include <iostream>
# include <math.h>
# include <vector>
# include <string>
# include <algorithm>
# include <unordered_map>
# define lli long long int
# define li long int
# define ld long double
using namespace std;

void take_input_vector(li n, vector<li> & elements){
	int input;
	for (size_t i = 0; i < n; i++){
		cin >> input;
		elements.push_back(input);
	} 
}

void print_vector(vector <li> const & vec){
	for (auto e: vec){
		cout << e << " ";
	}
}

void print_ump(unordered_map <li, li> const & ump){
	cout << "printing ump" << endl;
	for (auto e: ump){
		cout << e.first << " " << e.second << endl;
	}
}

		
void two_sum(li target, vector <li> & elements, unordered_map < li, li> & ump){
	li diff;
	for (size_t S = 0; S < elements.size(); S++){
		diff = target - elements[S];
		for (auto itr = ump.begin(); itr != ump.end(); itr++){
			if (diff == itr -> second){
				cout << S << " " << itr -> first << endl;
				break;
			}
			else{
				ump.insert({S, elements[S]});
			}
			print_ump(ump);
		}
	}
}

		
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	li n, target;
	vector <li> elements;
	unordered_map <li, li> ump;

	cin >> n >> target;
	take_input_vector(n, elements);
	// print_vector(elements);
	two_sum(target, elements, ump);
	return 0;
}
