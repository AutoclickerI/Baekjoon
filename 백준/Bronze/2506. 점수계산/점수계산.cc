#include<iostream>
using namespace std;
int main(){
    int N,n,c=1,s=0;
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>n;
        if(n){
            s+=c;
            c+=1;
        }
        else c=1;
    }
    cout<<s;
}