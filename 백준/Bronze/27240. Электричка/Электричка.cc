#include <iostream>
using namespace std;
 
int main(){
    long long n, a, b, s, t;
    cin >> n >> a >> b;
    cin >> s >> t;
    
    // Тариф "City": обе станции находятся в городе (между a и b)
    if(s > a && s < b && t > a && t < b) {
        cout << "City";
    }
    // Тариф "Outside": обе станции находятся в области и маршрут не проходит через город
    else if((s <= a && t <= a) || (s >= b && t >= b)) {
        cout << "Outside";
    }
    // В остальных случаях тариф "Full"
    else {
        cout << "Full";
    }
    return 0;
}
