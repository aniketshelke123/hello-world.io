# include <iostream>
# include <vector>
using namespace std;

int main (){

	auto vec = std::vector<int> {1, 2, 3, 4, 5};
	
	for (int i = 0; i < 5 ; i ++ ){
		cout << *(vec.rbegin() + i );
	}
	return 0;
}
