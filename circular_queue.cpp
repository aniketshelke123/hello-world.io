
# include <iostream>

using namespace std;


struct queue{
    int size;
    int rear;
    int front;
    int *Q;
};

void enqueue(struct queue *qu, int item){
    if ((qu -> rear + 1) % qu -> size == qu -> front){
        cout << "\n Queue is full..!!!" << endl;
    }
    else{
        qu -> rear = (qu -> rear + 1) % qu -> size;
        qu -> Q[qu -> rear] = item;
        cout << "\nItem Inserted..!!" << endl;
        cout << endl;
    }
}

int deque(struct queue *qu){
    int x = -1;
    if (qu -> front == qu -> rear){
        return 0;
    }
    else{
        qu -> front = (qu -> front + 1) % qu -> size;
        x = qu -> Q[qu -> front];
    }
    return x;
}

void display(struct queue qu){
    int i = qu.front + 1;
    do {
        cout << qu.Q[i] << " ";
        i = (i + 1) % qu.size;
    }while(i != (qu.rear + 1) % qu.size);
    cout << endl;
}

int main()
{
    struct queue qu;
    cout << "Enter size of queue: ";
    cin >> qu.size;
    qu.Q = new int[qu.size];
    qu.front = 0;
    qu.rear = 0;
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

