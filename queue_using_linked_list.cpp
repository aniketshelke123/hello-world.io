# include <iostream>

using namespace std;

struct queue{
    int data;
    struct queue *next;
};
struct queue *rear =  nullptr;
struct queue *front = nullptr;

void enqueue(int item){
    struct queue *temp;
    temp = new queue();
    if (temp == nullptr){   // if full..
        cout << "\n>> Queue is Full.!";
        cout << endl;
    }
    else{
        temp -> data = item;
        temp -> next = nullptr;
        if (front == nullptr)    // if empty
        {
            front  = rear = temp;
        }
        else{
            rear -> next = temp;
            rear = temp;
        }
        cout << "\n Item Inserted..!!";
        cout << endl;
    }
}

int deque(){
    int x = -1;
    struct queue *temp;
    if (front == nullptr){   // if empty...
        return 0;
    }
    else{
        temp = front;
        front = front -> next;
        x = temp -> data;
        delete temp;
    }
    return x;
}

void display(){
    struct queue *temp = front;
    cout << " \n The Data is: ";
    while (temp != rear -> next){
        cout << temp -> data << " ";
        temp = temp -> next;
    }
    cout << endl;
}

void Empty(){
    if (front == nullptr){
        cout << "empty" << endl;
    }
    else{
        cout << "mot empty" << endl;
    }
}

int main()
{
 
    int ch, item;
    do {
        cout << "1.ENQUEUE" <<  endl;
        cout << "2.DEQUE" << endl;
        cout << "3.DISPLAY" << endl;
        cout << "4.IS Empty" << endl;
        cout << "5. EXIT" << endl; 
        cout << "Enter your choice: ";
        cin >> ch;

        switch (ch)
        {
        case 1: cout << "Enter ele to push: ";
                cin >> item;
                enqueue(item);
                break;
        
        case 2: if (deque()){
                    cout << "\n>>> Deleted..!! " << endl;
                }
                else{
                    cout << "\n>>> Queue is empty..!" << endl;
                }
                cout << endl;
                break;
        case 3: display();
                break;
                
        case 4: Empty();
                cout << endl;
                break;
        case 5: exit(0);
                break;
            }
    }while(1);
    return 0;
}

