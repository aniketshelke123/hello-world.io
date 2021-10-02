
# include <iostream>
# include <vector>

using namespace std;
int p;
int check(vector<int> elements, int d){
    int value, p;
    for (int i = 0; i < elements.size(); i++){
        for (int j = i + 1; j < elements.size(); j ++){
            if (elements[i] + elements[j] <= d){
                value = (elements[i] + elements[j]);
                // cout << "value is " << value << endl;
                return value;
            // return elements[i];
            }    
            // else if (elements[i] == d){
            //     value = elements[i];
            //     return value;
            // }
            // else if (elements[i] > d){
            //     value = elements[i];
            //     return p;
            // }   
        }
    }
    return false;
}


int main()
{
    int test_cases, n, d, input, replace, k;
    // int win = 0, lose = 0;
    vector<int> elements;
    cin >> test_cases;
    k = 1;
    while (k <= test_cases){
        int win = 0, lose = 0;
        cin >> n >> d;

        for (int i = 0; i < n; i++)
        {
            cin >> input;
            elements.push_back(input);

        replace = check(elements, d);
        // cout << "replace " << replace << endl;
        for (int i = 0; i < elements.size(); i++){
            if (elements[i] >= d){
                // replace = check(elements, d);
                if (replace){
                    // cout << elements[i] << endl;
                    elements[i] = replace;
                    win += 1;
                }
            
                else if (replace == false){
                    if (elements[i] > d){
                        lose += 1;
                    }
                    // else if (elements[i] <= d)
                    // {
                    //     win += 1;
                    // }
                    
                }
            }
        }
        // cout << "\nwin" << win << endl;
        // cout << "lose" << lose<< endl;
        // cout << "\n";
        if (win > lose){
            cout << "Yes"<< endl;
            // win = 0;
            // lose = 0;
        }
        else if (lose > 1){
            cout << "No" << endl;
            // win = 0;
            // lose = 0;
        }
        // else if (lose == 1){
        //     cout <<"yes" << endl;
        // }
        else if (win == lose){
            cout << "yes" << endl;
            // win = 0;
            // lose = 0;
        }
        else if (lose == 1){
        cout << "No" << endl;
        }
        // cout << "The elemnts are:" << endl;
        // for (int i=0; i<elements.size(); i++)
        // {
        //     cout << elements [i] << " ";
        //     cout << endl;
        // }
        elements.clear();

        win = 0;
        lose = 0;
        // cout << win << lose;
        k += 1;
    }
    return 0;
}