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
        // cout << "\n Item Inserted..!!";
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

int Empty(){
    if (front == nullptr){
        return 1;
    }
    return 0;
}

void BFS(int G[7][7], int start, int n){
    int i = start, j;
    int visited[n] = {0};
    cout << i;
    visited[i] = 1;
    enqueue(i);
    while(!Empty())
    {
        i = deque();
        for(j = 1; j < n; j++)
        {
            if(G[i][j] == 1 && visited[j] == 0)
            {
                cout << j;
                visited[j] = 1;
                enqueue(j);
            }
        }
    }
}


void DFS(int G[][7], int start, int n){
    static int visited[7] = {0};
    int j;
    if(visited[start] == 0){
        cout << start << " ";
        visited[start] = 1;

        for(j = 1; j < n; j++){
            if(G[start][j] == 1 && visited[j] == 0)
                DFS(G, j, n);
        }
    }
}

int main()
{
    int G[7][7] = {{0,0,0,0,0,0,0},
                  {0,0,1,1,0,0,0},
                  {0,1,0,0,1,0,0},
                  {0,1,0,0,1,0,0},
                  {0,0,1,1,0,1,1},
                  {0,0,0,0,1,0,0},
                  {0,0,0,0,1,0,0}};

    // BFS(G, 4, 7);   // 1 is start and 7 is no. of vertices
    DFS(G, 4, 7);
    return 0;
}
