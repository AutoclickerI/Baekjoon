#include <iostream>
int main(){
    int a,s=0,b,c;
    std::cin>>a;
    while(a--){std::cin>>b>>c;s+=c%b;}
    std::cout<<s;
}