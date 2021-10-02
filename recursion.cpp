
# include <iostream>

using namespace std;
void fun(int y){
    if (y > 0){
        // cout << y << endl;
        fun(y - 1);
        cout << y << endl;
    }
}

int main()
{
    int x = 3;
    fun(3);
    return 0;
}
