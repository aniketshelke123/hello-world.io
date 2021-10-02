# include <iostream>

using namespace std;

struct stack{
    int size;
    int top;
    int *s;
};

int stack_top(stack st){
    if (st.top == -1){
        return -1;
    }
    else{
        return st.s[st.top];
    }
}

int Empty(stack st){
    if (st.top == -1){
        return 0;
    }
    return 1;
}

int is_Full(stack st){
    if (st.top == st.size - 1){
        return 1;
    }
    return 0;
}

void push(struct stack *st, int item){
    if (st -> top == st -> size - 1){   // its Full.....
        cout << "\nStack Overflow" << endl;
    }
    else{
        st -> top++;
        st -> s[st -> top] = item;
        cout << "\n >>>> Item pushed..!!" << endl;
        cout << endl;
    }
}

int pop(struct stack *st){
    int ele = -1;
    if (st -> top == -1){ // its empty.....
        return 0;
    }
    else{
        ele = st -> s[st -> top];
        st -> top--;
        return ele;
    }
}

int peek(struct stack st, int pos){
    int x = -1;
    if (st.top - pos + 1 < 0){
        return 0;
    }
    else{
        x = st.s[st.top - pos + 1];
        return x; 
    }
}

void traverse(struct stack st){
    if (st.top == -1){
        cout << "\n >> Stack is empty..!!" << endl;
        cout << endl;
    }
    else{
        cout << "\nStack elements are: ";
        for (int i = 0; i <= st.top; i++){
            cout << st.s[i] << " " ;
        }
        cout << endl;
        cout << endl;
    }
}

int main()
{
    int ch, item, pos;
    struct stack st;
    cout << "Enter the size of stack: ";
    cin >> st.size;
    st.s = new int[st.size];
    st.top = -1;
    do {
        cout << "1.PUSH" <<  endl;
        cout << "2.POP" << endl;
        cout << "3.PEEK" << endl;
        cout << "4.TRAVERSE" << endl;
        cout << "5.StackTop" << endl;
        cout << "6.Is Empty" << endl;
        cout << "7.Is FULL" << endl;
        cout << "8. EXIT" << endl; 
        cout << "Enter your choice: ";
        cin >> ch;

        switch (ch)
        {
        case 1: printf("Enter ele to push: ");
                scanf("%d", &item);
                push(&st, item);
                break;
        
        case 2: if (pop(&st)){
                    cout << "\n>>>Poped..!! " << endl;
                }
                else{
                    cout << "\n>>> Stack Underflow..!" << endl;
                }
                cout << endl;
                break;
        
        case 3: cout << "Enter position: ";
                cin >> pos;
                if (peek(st, pos)){
                    cout << "\nItem is: " << peek(st, pos) << endl;
                }
                else{
                    cout << "\n>> Invalid position..!!" << endl;
                    cout << endl;
                }
                break;
        case 4: traverse(st);
                break;

        case 5: cout << "\n>> Stack Top: " << (stack_top(st)) << endl;
                cout << endl;
                break;
        
        case 6: if (Empty(st)){
                    cout << "\n>> Not empty..!!\n";
                }
                else{
                    cout << "\n >> Empty..!!" << endl;
                }
                cout << endl;
                break;

        case 7: if (is_Full(st)){
                    cout << "\n>> Is Full..!!" << endl;
                }
                else{
                    cout << "\n >> Not Full..!!" << endl;
                    cout << endl;
                }
        case 8: exit(0);
                break;
        }
   }while(1);

    return 0;
}


