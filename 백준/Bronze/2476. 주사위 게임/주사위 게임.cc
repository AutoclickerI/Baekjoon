#include<iostream>
using namespace std;
int main(){
    int N,a,b,c,M=0,m;
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>a>>b>>c;
        if(a==b&&b==c)m=10000+1000*a;
        else if(a==b||a==c)m=1000+100*a;
        else if(b==c)m=1000+100*b;
        else if(a<c&&b<c)m=100*c;
        else if(a<b&&c<b)m=100*b;
        else m=100*a;
        if(M<m)M=m;
    }
    cout<<M;
}