#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<process.h>

struct node
{
	int ele;
	struct node *next;
};

struct node *first_node = NULL;


void insert_nn_at_first_position(struct node *temp, struct node *nn, struct node *first_node)
{
    temp = first_node;
    nn -> next = temp -> next;
    first_node -> next = nn;
    printf("\n Node inserted at first position sucessfully");
}

void insert_nn_at_last_position(struct node *temp,struct node *nn, struct node *first_node)
{
    temp = first_node;
    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    temp -> next = nn;
    // temp -> next = nn -> next;
    printf("\n Node is inserted at last position sucessfully\n");
}

void insert_nn_at_selected_position(struct node* temp, struct node* nn, struct node *first_node)
{
    temp = first_node;
    int n;
    printf("\n enter the element of the node before which you want insert the node: ");
    scanf("%d",&n);
    while(temp -> ele != n && temp -> next != NULL)
    {
        temp = temp -> next;
    }
    if(temp -> ele == n)
    {
        nn -> next = temp -> next;
        temp -> next = nn;
    }
    printf("\nthe node is inserted at selected position\n");
}

void insert_operation()
{
	int ch;
	struct node *temp;
	struct node *nn = (struct node *)malloc(sizeof(struct node));

	printf("Enter element for NEW NODE : ");
	scanf("%d", &nn->ele);
	nn->next = NULL;

    if(first_node==NULL)
    {
        first_node = nn; 
    }
    else
    {
        printf("\t1 - INSERT NEW NODE AT FIRST POSITION\n");
        printf("\t2 - INSERT NEW NODE AT LAST POSITION\n");
        printf("\t3 - INSERT NEW NODE AT SELECTED POSITION\n");
	    printf("\tProvide your choice : ");
	    scanf("%d",&ch);
	    switch(ch)
	    {
	    	case 1: insert_nn_at_first_position(temp,nn, first_node);
    	    		break;

    		case 2: insert_nn_at_last_position(temp,nn, first_node);
        			break;

    		case 3: insert_nn_at_selected_position(temp, nn, first_node);
        			break;

	    } // end of switch-case
    } //end of else
} //end of insert_operation()



void remove_first_node(struct node *temp)
{
    temp=first_node;
    first_node=first_node->next;
    free(temp);
    printf("\n first node is removed successfully");
}

void remove_last_node(struct node* temp)
{
    struct node* temp2;
    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    temp2=first_node;
    while(temp2->next!=temp)
    {
        temp2=temp2->next;
    }
    temp2->next=NULL;
    free(temp);
    printf("\n Node removed sucessfully from list");
}

void remove_selected_node(struct node* temp)
{
    struct node *ptr,*temp2;
    int n;
    printf("enter the node element which you want to remove:");
    scanf("%d",&n);
    while(temp->ele!=n && temp->next!=NULL)
    {
        temp=temp->next;
    }
    ptr=temp->next;
    temp->next=NULL;
    temp2=first_node;

    while(temp2->next!=temp)
    {
        temp2=temp2->next;
    }
    temp2->next=ptr;
    printf("\nslected node removed successfully");
}

void remove_operation()
{    
    struct node* temp;
	int ch;
	printf("\t1 - REMOVE FIRST NODE\n");
	printf("\t2 - REMOVE LAST NODE\n");
	printf("\t3 - REMOVE SELECTED NODE\n");
	printf("\tProvide your choice : ");
	scanf("%d", &ch);
	switch(ch)
	{
		case 1: remove_first_node(temp);
			break;

		case 2: remove_last_node(temp);
			break;

		case 3: remove_selected_node(temp);
			break;

	} //end of switch-case
} //end of remove_operation()



void display()
{  
    struct node* temp;
    if(first_node==NULL)
    {
        printf("\nlist yet not created");
    }
    else
    {
        printf("\nlist elements are:");
        temp=first_node;
        while(temp!=NULL)
        {
            printf("%d\t",temp->ele);
            temp=temp->next;
        }
        printf("\n");
    }
} //end of display()

int main()
{
    struct node* temp;
    int ch;
    
    do
    {
		printf("1 - INSERT OPERATION\n");
		printf("2 - REMOVE OPERATION\n");
		printf("3 - DISPLAY\n");
		printf("4 - EXIT\n");
		printf("Provide your choice : ");
		scanf("%d", &ch);

		switch(ch)
		{
			case 1: insert_operation();
				break;
			case 2: remove_operation();
				break;
			case 3: display();
				break;
			case 4: exit(0);
		} //end of switch
	 }while(1);
	 getch();
}
