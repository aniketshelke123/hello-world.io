
# include <iostream>
# include <vector>c
using namespace std;

struct Node{
    int data;
    struct Node *right;
    struct Node *left;
};
Node *root = nullptr;

void insert_nn_at_first_position(){
    struct Node *temp;
    temp = new Node();
    cout << "Enter data: ";
    cin >> temp -> data;
    temp -> right = nullptr;
    temp -> left = nullptr;

    if (root == nullptr){
        root = temp;
    }
    else{    // adds node at first position..........
        temp -> right = root;
        root -> left = temp;
        root = temp;
    }
}

void insert_nn_at_last_position(){
    struct Node *temp;
    temp = new Node();
    cout << "Enter data: ";
    cin >> temp -> data;

    temp -> right = nullptr;
    temp -> left = nullptr;

    if (root == nullptr){
        root = temp;
    }
    else{  //adds node at last of list position............
        struct Node *p;
        p = root;
        while (p -> right != nullptr){
            p = p -> right;
        }
        p -> right = temp;
        temp -> left = p;
    }
}

void insert_nn_at_selected_position(){
    struct Node *temp, *p = root;
    int length();
    int loc, len, i = 1;

    cout << "Enter the loc to add: ";
    cin >> loc;

    len = length();
    if (loc >= len){
        cout << "\n Invalid loaction..!!" << endl;
    }
    else{
        temp = new Node();
        cout << "Enter Data: " ;
        cin >> temp -> data;

        temp -> right = nullptr;
        temp -> left = nullptr;

        while (i < loc){
            p = p -> right;
        }        
        temp -> right = p -> right;
        p -> right -> left = temp;
        temp -> left = p;
        p -> right = temp;
    }
}


void insert(){
    int ch;
    cout << "\t1. Insert new node at FIRST position: " << endl;
    cout << "\t2. Insert new node at LAST position: " << endl;
    cout << "\t3. Insert new node at SELECTED position: " << endl;
    cout << "\nProvide your choice: ";
    cin >> ch;
    switch (ch)
    {
    case 1: insert_nn_at_first_position();
            break;
    
    case 2: insert_nn_at_last_position();
            break;
    
    case 3: insert_nn_at_selected_position();
            break;
    }
}

void remove_first_node(){
    struct Node *temp = root;
    int length();
    int len = length();

    if (len > 0){
        if (len > 1)
            root = root -> right;
            root -> left = nullptr;
            delete temp;
            cout << "\nDATA deleted..!!" << endl;
    }
    else{
        cout << "\n Data is empty..!!" << endl;
    }
}

void remove_last_node(){
    int element;
    struct Node *temp = root, *p;

    while (temp -> right -> right != nullptr){
        temp = temp -> right;
    }
    p = temp -> right;
    temp -> right = p -> right;
    delete p;
}

void remove_specific_node(){
    struct Node *temp = root, *p, *q;
    int element;
    cout << "Enter the element: ";
    cin >> element;

    while (temp -> right -> data == element && temp -> right != nullptr){
        temp = temp-> right;
    }
    p = temp -> left;
    q = temp -> right;
    p -> right = q;
    q -> left = p;
    delete temp;
}


void remove(){
    int ch;
    cout << "\t1 - REMOVE FIRST NODE" << endl;
    cout << "\t2 - REMOVE LAST NODE" << endl;
    cout << "\t3 - REMOVE SELECTED NODE" << endl;
    cout << "\tProvide your choice : ";
    cin >> ch;
    switch(ch)
    {
        case 1: remove_first_node();
                break;

        case 2: remove_last_node();
                break;

        case 3: remove_specific_node();
                break;
    }
}

int length(){
    struct Node *temp = root;
    int count  = 0;

    while (temp != nullptr){
        count ++;
        temp = temp -> right;
    }
    return count;
}


void display(){
    struct Node *temp = root;
    temp =  root;
    cout << "\nThe data is: ";
    if (temp == nullptr){
        cout << "List is empty..!!" << endl;
    }
    else{
        while (temp != nullptr){
            cout << temp -> data << " ";
            temp = temp -> right;
        }
        cout << endl;
    }
}

int main()
{
	int ch;
	do
	{
    	cout << "1 - INSERT OPERATION" << endl;
		cout << "2 - REMOVE OPERATION" << endl;
        cout << "3 - LENGTH" << endl;
		cout << "4 - DISPLAY" << endl;
		cout << "5 - REVERSE " << endl;
		cout << "6 - EXIT" << endl;
		cout << "Provide your choice : ";
		cin >> ch;

		switch(ch)
		{
			case 1: insert();
				    break;
			case 2: remove();
				    break;
            case 3: cout << "\nThe length is: " << length() << endl;
                    cout << endl;
                    break;
			case 4: display();
				    break;
            // case 7: reversing_using_sliding_pointers(temp);
            //         break;
            case 9: exit(0);
		} //end of switch
	 }while(1);

    return 0;
}
