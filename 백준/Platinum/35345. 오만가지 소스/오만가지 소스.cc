#include "sauce.h"
#include <bits/stdc++.h>
using namespace std;

vector<pair<int,int>> vranges;

vector<int> arrgenerator(vector<int> idxs) {
    vector<int> ret;
    for (auto& v : idxs) {
        auto& [s,e]=vranges[v];
        for (int i=s;i<e;i++)
            ret.push_back(i);
    }
    return ret;
}

int solve(int N) {
    int i=0,step,left,r=0;
    step=N/6;
    left=N%6;
    while (i<N){
        vranges.push_back(make_pair(i,min(i+step,N)+(0<left)));
        i+=step+(0<left);
        left--;
    }
    for (int i=0;i<6;i++) {
        for (int j=i+1;j<6;j++) {
            for (int k=j+1;k<6;k++)
                r+=query(arrgenerator({i,j,k}));
            r-=query(arrgenerator({i,j}))*3;
        }
        r+=query(arrgenerator({i}))*6;
    }
    return r;
}
