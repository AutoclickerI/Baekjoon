#include<iostream>
using namespace std;
int main(){
    int N,r,e,c;
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>r>>e>>c;
        if(r<e-c)cout<<"advertise\n";
        else if(r>e-c)cout<<"do not advertise\n";
        else cout<<"does not matter\n";
    }
}