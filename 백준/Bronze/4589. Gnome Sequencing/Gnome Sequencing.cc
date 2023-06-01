#include <iostream>
#include <vector>
using namespace std;
int main(){
    long int a,b,c,d;
    cin>>a;
    cout<<"Gnomes:"<<endl;
    vector<string> g={"Unordered","Ordered"};
    while(a--){
        cin>>b>>c>>d;
        cout<<g[(int)(((b<c)&&(c<d))||((b>c)&&(c>d)))]<<endl;
    }
}