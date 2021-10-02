
# include <iostream>
// return by addres....

using namespace std;

// int *fun(){
//     int *p = new int[5];
//     for (int i = 0; i < 5; i++){
//         p[i] = 5 * i;
//     }
//     return p;
int* fun() {
    int* p = new int[5];
    int* p1 = p;
    for (int i = 0; i < 5; i++,p++) {
        *p = 5 * i;
    }
    // p = p1;
    return p1;
}
int main()
{
    int *q = fun();
    for (int i = 0; i < 5; i++){
        cout << q[i] << endl;
    }
    delete q;
    return 0;
}
