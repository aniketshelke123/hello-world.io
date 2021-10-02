
# include <iostream>
using namespace std;

struct Node{
    int data;
    struct Node *next;
};
Node  *root = nullptr;

void insert_nn_at_selected_position(){
    struct Node *temp, *p = root;
    int length();
    int loc, len, i = 0;

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

        temp -> next = nullptr;
        if (root == nullptr){
            root = temp;
        }
        else{

        }
        while (i < loc){
            p = p -> next;
        }        
        temp -> next = p -> next;
        p -> right -> left = temp;
        temp -> left = p;
        p -> right = temp;
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
		// cout << "2 - REMOVE OPERATION" << endl;
        cout << "3 - LENGTH" << endl;
		cout << "4 - DISPLAY" << endl;
		// cout << "5 - REVERSE " << endl;
		cout << "6 - EXIT" << endl;
		cout << "Provide your choice : ";
		cin >> ch;

		switch(ch)
		{
			case 1: insert_nn_at_selected_position();
				    break;
			// case 2: remove();
			// 	    break;
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
