# include <bits/stdc++.h>
# include <iostream>
# include <math.h>
# include <vector>
# include <string>
# include <ctype.h>
# include <algorithm>
# define lli long long int
# define li long int
# define ld long double
using namespace std;

int position_1(vector <string> & bus_stops, string Source){
    for (int i = 0; i <= bus_stops.size(); i++){
        if (bus_stops[i] == Source){
            return i;
        }
    }
    return 0;
}

int position_2(vector <string> & bus_stops, string Destination){
    for (int i = 0; i <= bus_stops.size(); i++){
        if (bus_stops[i] == Destination){
            return i;
        }
    }
    return 0;
}

int sum_of_pos_1(int pos_1, vector <int> & paths){
    int length = paths.size();
    int sum1 = 0;
    for(int i = 0; i <= paths.size(); i++){
        if (i > pos_1 && i <= length - 1){
            sum1 += paths[i];
        }
    }
    return sum1;
}

int sum_of_pos_2(int pos_2, vector <int> & paths){
    int length = paths.size();
    int sum2 = 0;
    for (int i = 0; i <= paths.size(); i++){
        if (i <= pos_2){
            sum2 += paths[i];
        }
    }
    return sum2;
}

int get_distance(vector <string> & bus_stops, vector <int> & paths, string Source, string Destination){
    int pos_1 = position_1(bus_stops, Source);
    int pos_2 = position_2(bus_stops, Destination);
    int total_sum = (sum_of_pos_1(pos_1, paths) + sum_of_pos_2(pos_2, paths));
    return total_sum;
}

float total_travel_fare(vector <string> & bus_stops, vector <int> & paths, string Source, string Destination){
    int Distance = get_distance(bus_stops, paths, Source, Destination);
    float fare = (Distance / 200.0);
    return fare;
}

float getFare(vector <string> & bus_stops, vector <int> paths, string Source, string Destination){
    return round(total_travel_fare(bus_stops, paths, Source, Destination));
 }

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    vector <string> bus_stops = {"TH", "GA", "IC", "HA", "TE", "LU", "NI", "CA"};
    vector <int> paths = {800, 600, 750, 900, 1400, 1200, 1100, 1500};
    string Source, Destination;
    cin >> Source;
    cin >> Destination;
    int i = 0;
    if (isupper(Source[i]) && isupper(Destination[i])){
        float fare = getFare(bus_stops, paths, Source, Destination);
        cout << fare << ".0 INR" << endl;
    }
    else{
        cout << "INVALID INPUT" << endl;
    }
    return 0;
}
