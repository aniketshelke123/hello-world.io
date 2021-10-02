# include <iostream>

using namespace std;

struct Node{
    int data;
    struct Node *next;
};
Node *top = nullptr;


int stack_top(){
    if (top){
        return top -> data;
    }
    return -1;
}

int Empty(){
    return top ? 0 : 1;
}

int Full(){
    struct Node *temp;
    temp = new Node();
    int r = temp ? 1 : 0;
    delete temp;
    return r;
}

void push(int item){
    struct Node *temp;
    temp = new Node();

    if (temp == nullptr){
        cout << "\nStack Overflow..!!" << endl;
    }
    else{    // adds node at first position..........
        temp -> data = item;
        temp -> next =  top;
        top = temp;
        cout << "\n Item pushed..!" << endl;
        cout << endl;
    }
}

int pop(){
    int x = -1;
    if (top == nullptr){
        cout << "Stack Underflow..!!";
    }
    else{
        struct Node *p;
        p = top;
        top = top -> next;
        x = p-> data;
        delete p;
    }
    return x;
}

int peek(int pos){
    struct Node *p = top;
    for (int i = 0; i < pos - 1 && p != nullptr; i++){
        p = p -> next;
    }
    if (p != nullptr){
        return p -> data;
    }
    else{
        return -1;
    }
}

void traverse(){
    if (Empty()){
        cout << "\n >> Stack is empty..!!" << endl;
        cout << endl;
    }
    else{
        struct Node *temp = top;
        cout << "\nStack elements are: ";
//         // for (int i = 0; i <= top -> data; i++){
        while (temp != nullptr){
            cout << temp -> data << " " ;
            temp =  temp -> next;
            
        }
        cout << endl;
    }
}

int main()
{
	int ch, item, pos;
	do
	{
    	cout << "1 - PUSH" << endl;
		cout << "2 - POP" << endl;
        cout << "3 - PEEK" << endl;
		cout << "4 - Stack Top" << endl;
		cout << "5 - Empty " << endl;
		cout << "6 - FULL " << endl;
		cout << "7 - TRAVERSE " << endl;
		cout << "8 - EXIT" << endl;
		cout << "Provide your choice : ";
		cin >> ch;

		switch(ch)
		{
			case 1: cout << "\nEnter item: " ;
                    cin >> item;
                    push(item);
				    break;
			case 2: cout << "\nPop is: " << pop() << endl;
				    cout << endl;
                    break;
            case 3: cout << "\nEnter Position: ";
                    cin >> pos;
                    cout << "\nThe item is: " << peek(pos) << endl;
                    cout << endl;
                    break;
			case 4: cout << "\nStack top: " << stack_top() << endl;
                    cout << endl;
				    break;
            case 5: if (Empty()){
                        cout << "\n>> Empty\n";
                    }
                    else{
                        cout << "\n>> Not Empty..!!";
                    }
                    cout << endl;
                    break;

            case 6: if (Full()){
                        cout << "\n>> Not Full..!!";
                    }
                    else{
                        cout <<"\n>> Stack Full..!!";
                    }
                    cout << endl;
                    break;
            case 7: traverse();
                    break;

            case 8: exit(0);
		} //end of switch
    }while(1);

    return 0;
}