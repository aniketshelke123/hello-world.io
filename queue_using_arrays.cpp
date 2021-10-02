
# include <iostream>

using namespace std;


struct queue{
    int size;
    int rear;
    int front;
    int *Q;
};

void enqueue(struct queue *qu, int item){
    if (qu -> rear == qu -> size - 1){
        cout << "\n Queue is full..!!!" << endl;
    }
    else{
        qu -> rear++;
        qu -> Q[qu -> rear] = item;
        cout << "\nItem Inserted..!!" << endl;
        cout << endl;
    }
}

int deque(struct queue *qu){
    int x = -1;
    if (qu -> front == qu -> rear){
        // cout << "\n >> Queue is empty..!!" << endl;
        return 0;
    }
    else{
        qu -> front++;
        x = qu -> Q[qu -> front];
    }
    return x;
}

void display(struct queue qu){
    for (int i = qu.front + 1; i <= qu.rear; i++){
        cout << qu.Q[i] << " ";
    }
    cout << endl;
}

int main()
{
    struct queue qu;
    cout << "Enter size of queue: ";
    cin >> qu.size;
    qu.Q = new int[qu.size];
    qu.front = -1;
    qu.rear = -1;
    int ch, item;
    do {
        cout << "1.ENQUEUE" <<  endl;
        cout << "2.DEQUE" << endl;
        cout << "3.DISPLAY" << endl;
        cout << "4. EXIT" << endl; 
        cout << "Enter your choice: ";
        cin >> ch;

        switch (ch)
        {
        case 1: printf("Enter ele to push: ");
                scanf("%d", &item);
                enqueue(&qu, item);
                break;
        
        case 2: if (deque(&qu)){
                    cout << "\n>>>Poped..!! " << endl;
                }
                else{
                    cout << "\n>>> Queue is empty..!" << endl;
                }
                cout << endl;
                break;
        case 3: display(qu);
                break;
                
        case 4: exit(0);
                break;
            }
    }while(1);
    return 0;
}
