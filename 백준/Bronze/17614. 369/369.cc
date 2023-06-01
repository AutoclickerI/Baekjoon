#include<iostream>
using namespace std;
int main(){
    int N,a=0,t,i;
    cin>>N;
    for(int j=1;j<=N;j++){
		i=j;
        while(i){
            t=i%10;
            if(t==3||t==6||t==9)a++;
            i/=10;
        }
    }
    cout<<a;
}