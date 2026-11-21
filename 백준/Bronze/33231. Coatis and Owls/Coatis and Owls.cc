#include <iostream>
#include <vector>
using namespace std;
 
// Helper: compute ceil(a/b) for positive integers.
inline int ceilDiv(long long a, long long b) {
    return (int)((a + b - 1) / b);
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int n, m;
    cin >> n >> m;
    vector<int> coati(n), owl(m);
    for (int i = 0; i < n; i++){
        cin >> coati[i];
    }
    for (int j = 0; j < m; j++){
        cin >> owl[j];
    }
    
    // Pointers: for coati, i is the index of the front squad (rightmost);
    // for owl, j is the index of the front squad (leftmost).
    int i = n - 1, j = 0;
    
    while(i >= 0 && j < m){
        int c = coati[i];
        int o = owl[j];
        if(c == o){
            // Both squads annihilate each other.
            i--; j++;
        } else if(c > o){
            // Coati wins: it loses ceil(o^2 / c) pikemen.
            int loss = ceilDiv((long long)o * o, c);
            int newC = c - loss;
            // Owl squad is eliminated.
            j++;
            if(newC <= 0){
                // The coati squad is also eliminated.
                i--;
            } else {
                coati[i] = newC; // update surviving coati squad.
            }
        } else { // c < o
            // Owl wins: it loses ceil(c^2 / o) pikemen.
            int loss = ceilDiv((long long)c * c, o);
            int newO = o - loss;
            // Coati squad is eliminated.
            i--;
            if(newO <= 0){
                j++;
            } else {
                owl[j] = newO; // update surviving owl squad.
            }
        }
    }
    
    // Sum remaining pikemen on each side.
    long long sumCoati = 0, sumOwl = 0;
    if(i >= 0){
        // Squads 0..i in coati remain.
        for (int k = 0; k <= i; k++){
            sumCoati += coati[k];
        }
    }
    if(j < m){
        for (int k = j; k < m; k++){
            sumOwl += owl[k];
        }
    }
    
    if(sumCoati == 0 && sumOwl == 0){
        cout << "stalemate\n";
    } else if(sumCoati > 0 && sumOwl == 0){
        cout << "coatis\n" << sumCoati << "\n";
    } else if(sumOwl > 0 && sumCoati == 0){
        cout << "owls\n" << sumOwl << "\n";
    }
    return 0;
}
