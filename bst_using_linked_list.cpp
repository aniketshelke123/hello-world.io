
# include <iostream>

using namespace std;

struct Node{
    int data;
    struct Node *left;
    struct Node *right;
};
struct Node *root = nullptr, *t;

void insert(){
    struct Node *temp, *parent;
    temp = new Node();
    cout << "Enter the data: ";
    cin >> temp -> data;
    temp -> right = nullptr;
    temp -> left = nullptr;
    if (root == nullptr){
        root = temp;
        t = root;
        cout << "\n Data inserted..!!" <<  endl;
    }
    else{
        struct Node *current;
        current = root;
        while(current){
            parent = current;
            if (temp -> data > current -> data){
                current = current -> right;
            }
            else{
                current = current -> left;
            }
	}

        //here parent is pointing to last node 
        if (temp -> data > parent -> data){ // if data > parent
            parent -> right = temp;
        }
        else{                               // if data < parent
            parent -> left = temp;
        }
    cout << "\nData inserted..!!" << endl;
    }
}


void inorder(struct Node *t){
    if (t -> left){
        inorder(t -> left);
    }
    cout << t -> data << " ";
    if (t -> right){
        inorder(t -> right);
    }
}

void Delete(){
    int item, check;
    cout << "Enter the item: ";
    cin >> item;
    struct Node *current = root, *parent;
    while (current -> data != item){
        parent = current;
        if (item > current -> data){
            current = current -> right;
        }
        else{
            current = current -> left;
        }
    }
    // logic for deleting leaf node
    if (current -> right == nullptr && current -> left == nullptr){
        if (current == parent -> right){  
            parent -> right = nullptr;
        }
        else{
            parent -> left = nullptr;          
        }
        delete current;                   // ends here....... 
    }
    // logic for deleting child nodes on one side of current node.....
    else if (current -> left != nullptr && current -> right == nullptr){     
        if (current == parent -> right){
            parent -> right = current -> left;
        }
        else{
            parent -> left = current -> left;
        }
        current -> left = nullptr;
        delete current;
    }
    else if (current -> right != nullptr && current -> left == nullptr){
        if (current == parent -> right){
            parent -> right = current -> right;
        }
        else{
            parent -> left = current -> right;
        }
        current -> right = nullptr;
        delete current;
    }                                      // ends here......
    // logic for deleting child nodes on both sides of current node.....
    else if (current -> left != nullptr && current -> right != nullptr){
        struct Node *temp1, *temp2;
        temp1 = current -> right;
        if (temp1 -> left == nullptr && temp1 -> right == nullptr){
            current -> data = temp1 -> data;
            current -> right = nullptr;
            delete temp1;
        }
        else if (temp1 -> right != nullptr && temp1 -> left == nullptr){
            current -> data = temp1 -> data;
            current -> right = temp1 -> right;
            temp1 -> right = nullptr;
            delete temp1;
        }
        else if (temp1 -> left != nullptr){
            while (temp1 -> left -> left != nullptr)
            {
                temp1 = temp1 -> left;
            }
            temp2 = temp1 -> left;
            current -> data = temp2 -> data;
            temp1 -> left = temp2 -> right;
            delete temp2;
        }
    }
}

int search(){
    struct Node *current = root, *temp;
    temp = new Node();
    cout << "Enter the item to be searched: ";
    cin >> temp -> data;
    temp -> left = nullptr;
    temp -> right = nullptr;
    while (current -> left != nullptr){
        if (temp -> data > current -> data){
            current = current -> right;
        }
        else if (temp -> data < current -> data){
            current = current -> left;
        }
    
        if (temp -> data == current -> data){
            return 1;
        }
    }
    return 0;
}

int main()
{ 

    int ch, item;
    do {
        cout << "\n1.INSERT" <<  endl;
        cout << "2.DELETE" << endl;
        cout << "3.DISPLAY" << endl;
        cout << "4.SEARCH" << endl;
        cout << "5. EXIT" << endl; 
        cout << "Enter your choice: ";
        cin >> ch;

        switch (ch)
        {
        case 1: insert();
                break;
        
        case 2: Delete();
                break;

        case 3: cout << endl;
                inorder(t);
                cout << endl;
                break;

         case 4: if (search()){
                cout << "\nItem found..!!" << endl;
                }
                else{
                    cout << "\nNot found..!! " << endl;
                }
                break;

        case 5: exit(0);
                break;
            }
    }while(1);

    
    return 0;
}
