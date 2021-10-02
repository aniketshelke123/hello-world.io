
# include <iostream>
using namespace std;

void swap(int *x,int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void bubble_sort(int A[], int n){
    int i, j, flag = 0;
    for(i = 0; i < n - 1; i++){
        flag = 0;
        for(j = 0; j < (n - i - 1); j++){
            if(A[j] > A[j + 1]){
                swap(&A[j], &A[j+1]);
                flag = 1;
            }
        }
        if (flag == 0){
            break;
        }
    }
}

int main()
{
    int A[] = {5, 2, 7, 9, 4, 1};
    int n = 6, i;
    bubble_sort(A, n);
    for(i=0;i<6;i++){
        printf("%d ",A[i]);
        printf("\n");
    }
    return 0;
}
