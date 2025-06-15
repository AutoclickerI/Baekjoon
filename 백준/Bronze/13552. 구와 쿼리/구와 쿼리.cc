#include<iostream>
using namespace std;

int p[100000][3];

int main(){
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
    int N,M,x,y,z,a;
    long long dx,dy,dz,r;
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>x>>y>>z;
        p[i][0]=x;p[i][1]=y;p[i][2]=z;
    }
    cin>>M;
    for(int i=0;i<M;i++){
        a=0;
        cin>>x>>y>>z>>r;
        for(int j=0;j<N;j++){
            dx=p[j][0]-x;dy=p[j][1]-y;dz=p[j][2]-z;
            a+=dx*dx+dy*dy+dz*dz<=r*r;
        }
        cout<<a<<"\n";
    }
}