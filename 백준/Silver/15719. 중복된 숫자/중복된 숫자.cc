#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    long long n, v, r=0;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>v;
        r+=v;
    }
    cout<<r-n*(n-1)/2;
}