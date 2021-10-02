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


int main(){

    	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, q, size, ele, y, x;
	cin >> n >> q;
	vector<vector<int>> Vec(n);
	for (int i =0; i < n; i++){
		cin >> size;
		for (int j = 0; j < size; j++){
			cin >> ele ;
			Vec[i].push_back(ele);
		}
	}

	for (int i = 0; i < q; i++){
		cin >> x >> y;
		cout << Vec[x].at(y) << endl;
	}

	return 0;
}
