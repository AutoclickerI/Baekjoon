#include <iostream>
using namespace std;
int main(){
    int a,x,y,Q1=0,Q2=0,Q3=0,Q4=0,axis=0;
    cin>>a;
    for (int i=a; i>0; i--){
        cin>>x>>y;
        if (x*y==0)axis++;
        else if ((x>0)*(y>0))Q1++;
        else if ((x>0)*(y<0))Q4++;
        else if (x*y>0)Q3++;
        else Q2++;
    }
    cout<<"Q1: "<<Q1<<endl<<"Q2: "<<Q2<<endl<<"Q3: "<<Q3<<endl<<"Q4: "<<Q4<<endl<<"AXIS: "<<axis;
}