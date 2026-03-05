#include <bits/stdc++.h>
using namespace std;

int kadane(vector<int> arr) {
    int m=0,v=0;
    for (auto& i : arr) {
        v=max(v,0)+i;
        m=max(v,m);
    }
    return m;
}

int main(){
    int N,M,v,r=0;
    cin>>N>>M;
    vector<vector<int>> b(N);
    for (int i=0;i<N;i++)
        for (int j=0;j<M;j++) {
            cin>>v;
            b[i].push_back(v);
        }
    for (int i=0;i<N;i++){
        vector<int> arr(M,0);
        for (int j=i;j<N;j++){
            for (int k=0;k<M;k++)
                arr[k]+=b[j][k];
            r=max(r,kadane(arr));
        }
    }
    cout<<r;
}