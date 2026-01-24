#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

#define CUT 64
#define CHUNK 16

using vll = vector<__int128>;

int max(int a, int b){
    return a<b?b:a;
}

vll parse(string s, int size){
    vll ret(size,0);
    int end=size;
    for(int i=s.size();0<i;i-=CHUNK){
        end-=1;
        int sv=max(0,i-CHUNK);
        ret[end]=stoll(s.substr(sv,i-sv));
    }
    return ret;
}

vll poly_add(vll a, vll b, int size){
    vll ret(size);
    for(int i=0; i<size;i++)
        ret[i]=a[i]+b[i];
    return ret;
}

vll poly_mul_naive(vll a, vll b, int size){
    vll ret(size*2,0);
    for(int i=0; i<size;i++)
        for(int j=0;j<size;j++)
            ret[i+j+1]+=a[i]*b[j];
    return ret;
}

vll karatsuba(vll a, vll b, int size){
    if(size<=CUT)
        return poly_mul_naive(a,b,size);
    int half=size>>1;
    vll a0(a.begin(), a.begin() + half);
    vll a1(a.begin() + half, a.end());
    vll b0(b.begin(), b.begin() + half);
    vll b1(b.begin() + half, b.end());
    vll z0=poly_add(a0,a1,half);
    vll z1=poly_add(b0,b1,half);
    vll p0=karatsuba(a0,b0,half);
    vll p1=karatsuba(z0,z1,half);
    vll p2=karatsuba(a1,b1,half);
    vll ret(size*2,0);
    for(int i=0;i<size;i++){
        ret[i]+=p0[i];
        ret[i+half]+=p1[i]-p0[i]-p2[i];
        ret[i+size]+=p2[i];
    }
    return ret;
}

void normalize(vll &r, int size){
    long long chunk=1;
    for(int i=0;i<CHUNK;i++)
        chunk*=10;
    for(int i=size-1;0<i;i--){
        r[i-1]+=r[i]/chunk;
        r[i]%=chunk;
    }
}

int main(){
    string s1, s2;
    cin>>s1>>s2;
    int size=(max(s1.size(),s2.size())+CHUNK-1)/CHUNK;
    int size_2=1;
    while(size_2<size)
        size_2<<=1;
    vll a=parse(s1,size_2), b=parse(s2,size_2);
    vll v=karatsuba(a,b,size_2);
    normalize(v,size_2*2);
    int i=0;
    while(v[i]==0 && i<size_2*2-1)
        i++;
    cout<<(long long)v[i];
    i++;
    while(i<size_2*2){
        cout<<setw(CHUNK)<<setfill('0')<<(long long)v[i];
        i++;
    }
    cout<<endl;
}