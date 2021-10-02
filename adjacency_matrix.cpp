
/* CPP code for adjacency matrix 
    Graph implementation using adjacency matrix*/

#include <iostream>
using namespace std;

int main()
{
    int A[5][5];
    int i,j;

    for(i=0;i<5;i++)
        for(j=0;j<5;j++)
            A[i][j]=0; /*Initializing the array A*/
            
    /*Creating adjacency matrix*/
    A[0][0]=1;
    A[0][1]=1;
    A[0][3]=1;
    A[1][2]=1;
    A[2][4]=1;
    A[3][2]=1;

    /*Printing Adjacency Matrix*/
    cout << "Adjacency Matrix:" << endl;
    for(i=0;i<5;i++)
    {
        cout << endl;
        for(j=0;j<5;j++){
            cout << A[i][j] << " ";
        }
    }
    cout << endl;
    return 0;
}
