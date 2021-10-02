
# include <iostream>
# include <algorithm>
# include <numeric>

using namespace std;


struct Node{
    int data;
    struct Node *next;
};
Node *root = nullptr, *temp;

void insert_nn_at_first_position(struct Node *temp, struct Node *nn, struct Node *root){
    temp = root;
    nn -> next = temp -> next;
    root -> next = nn;
    cout << "\nNew node inserted at first position.!!\n";
}

void insert_nn_at_last_position(struct Node *temp, struct Node *nn, struct Node *root){
    temp = root;
    while (temp -> next != nullptr){
        temp = temp -> next;
    }
    temp -> next = nn;
    cout << "\nNew node inserted at last position.!\n";
}

void insert_nn_at_selected_position(struct Node *temp, struct Node *nn, struct Node *root){
    temp = root;
    int n;
    cout << "Enter the element after you want to insert the new node: ";
    cin >> n;
    while (temp -> data != n && temp -> next != nullptr){
        temp = temp -> next;
    }
    if (temp -> data == n){
        nn -> next = temp -> next;
        temp -> next = nn;
        cout << "\nNode is inserted at selected position!" << endl;
    }
}

void insert(struct Node *temp){
    struct Node *nn;
    int ch;
    nn = new Node();
    // temp = new Node();
    cout << "enter element for new node: ";
    cin >> nn -> data;
    nn -> next = nullptr;

    if (root == nullptr){
        root = nn;
        cout << endl;
    }
    else{
        cout << "1. Insert new node at FIRST position: " << endl;
        cout << "2. Insert new node at LAST position: " << endl;
        cout << "3. Insert new node at SELECTED position: " << endl;
        cout << "\nProvide your choice: ";
        cin >> ch;
        switch (ch)
        {
        case 1: insert_nn_at_first_position(temp, nn, root);
                break;
        
        case 2: insert_nn_at_last_position(temp, nn, root);
                break;
        
        case 3: insert_nn_at_selected_position(temp, nn, root);
                break;
        }
    }
    // delete nn;
}


void remove_first_node(struct Node *temp)
{
    if (root == nullptr){
        cout << "No node present..!!" << endl;
    }
    else{
        temp = root;
        root = temp -> next;
        temp -> next = nullptr;
        delete temp;
        cout << "\n first node is removed successfully" << endl;
    }
}
void remove_last_node(struct Node *temp)
{
    struct Node *p;
    temp = root;
    while(temp -> next->next != nullptr)
    {
       temp = temp -> next;
    }
    p = temp -> next;
    temp -> next = p -> next;
    // p = nullptr;
    delete p;

    cout << "\n Node removed sucessfully from list" << endl;
}

void remove_selected_node(struct Node* temp)
{
    struct Node *p;
    temp =  root;
    int n;
    cout << "enter the node element which you want to remove: ";
    cin >> n;
    while(temp -> next-> data != n && temp -> next != nullptr)
    {
        temp = temp -> next;
    }
    p = temp -> next;
    temp -> next = p -> next;
    // p -> next = nullptr;
    delete p;

    cout << "\nselected node removed successfully" << endl;
}

void remove_operation(struct Node *temp)
{        
    if (root == nullptr){
        cout << "\nNo node present..!!\n" << endl;
    } 
    else{
        int ch;
        cout << "\t1 - REMOVE FIRST NODE" << endl;
        cout << "\t2 - REMOVE LAST NODE" << endl;
        cout << "\t3 - REMOVE SELECTED NODE" << endl;
        cout << "\tProvide your choice : ";
        cin >> ch;
        switch(ch)
        {
            case 1: remove_first_node(temp);
                    break;

            case 2: remove_last_node(temp);
                    break;

            case 3: remove_selected_node(temp);
                    break;

        } //end of switch-case
    }
} //end of remove_operation()

void add_after_using_loc(struct Node *temp){
    struct Node *nn;
    nn = new Node();
    int length(Node *temp);
    temp = root;
    struct Node *p;
    int len, loc, i = 1;
    cout << "Enter location: ";
    cin >> loc;
    cout << "Enter new node: ";
    cin >> nn -> data;
    len = length(temp);

    if (loc > len){
        cout << "\nInvalid location..!" << endl;
        cout << "Current list is having nodes: " << len << endl;
    }
    else{
        p = root;
        while (i < loc){
            p = p -> next;
            i++;
        }
        nn -> next = p -> next;
        p -> next = nn;
        cout << "\nNew node added successfullt.!" << endl;
    }
}

void delete_using_loc(struct Node *temp){
    int loc, len;
    int length(Node *temp);
    cout << "Enter loc to detele: ";
    cin >> loc;
    len = length(temp);
    
    if (loc > len){
        cout << "\nInvalid location.!" << endl;
    }
    else if (loc == 1){
        temp = root;
        root  = temp -> next;
        temp -> next = nullptr;
        delete temp;
        cout << "\nNode Deleted..!! " << endl;
    }
    else{
        struct Node *p = root, *q;
        int i = 1;
        while (i < loc - 1){
            p = p -> next;
        }
        q = p -> next;
        p -> next = q -> next;
        q -> next = nullptr;
        delete q;
        cout << "\nNode Deleted.!!" << endl;
    }
}

int length(struct Node *temp){
    int count  = 0;
    temp = root;
    while (temp != nullptr){
        count ++;
        temp = temp -> next;
    }
    // cout << "length: " << count  << endl;
    return count;
}

void reversing_using_sliding_pointers(struct Node *temp){
    struct Node *q = nullptr, *r = nullptr;
    temp =  root;
    while (temp != nullptr){
        r = q;
        q = temp;
        temp = temp -> next;
        q -> next = r;
    }
    root = q;
    cout << "\n Linked list reversed..!!" << endl;
}


void swap(struct Node *temp){ // the next two num after the loc gets swapped
    struct Node *q, *r;
    int i = 1, loc;
    cout << "Enter the location to swap data: ";
    cin  >> loc;
    temp = root;
    while(i < loc && temp != nullptr){
        temp = temp -> next;
        i++;
    }
    q = temp -> next;
    r = q -> next;
    q -> next = r -> next;
    r -> next = q;
    temp -> next = r;

}
void display(struct Node *temp){
    if (root == nullptr){
        cout << "\nNo nodes in list.!" << endl;
    }
    else{
        cout << endl;
        temp = root;
        while (temp != nullptr){
            cout << temp -> data << " ";
            temp = temp -> next;
        }
        cout << endl;
    }
    // cout << endl;

    // while(root == temp){
    //     cout << root -> data << endl;
    //     root  = root -> next;
    // }
} //display ends

int main()
{
    // struct Node *temp;
    // temp = new Node();
	int ch;

	do
	{
    	cout << "1 - INSERT OPERATION" << endl;
		cout << "2 - REMOVE OPERATION" << endl;
        cout << "3 - LENGTH" << endl;
		cout << "4 - DISPLAY" << endl;
		cout << "5 - ADD using location" << endl;
		cout << "6 - DELETE using location" << endl;
		cout << "7 - REVERSE " << endl;
		cout << "8 - SWAP " << endl;
		cout << "9 - EXIT" << endl;
		cout << "Provide your choice : ";
		cin >> ch;

		switch(ch)
		{
			case 1: insert(temp);
				    break;
			case 2: remove_operation(temp);
				    break;
            case 3: cout << "\n" << length(temp) << endl;
                    break;
			case 4: display(temp);
				    break;
            case 5: add_after_using_loc(temp);
                    break;
			case 6: delete_using_loc(temp);
                    break;
            case 7: reversing_using_sliding_pointers(temp);
                    break;
            case 8: swap(temp);
                    break;
            case 9: exit(0);
		} //end of switch
	 }while(1);

    return 0;
}