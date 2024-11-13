
#include <iostream>
#include<stack>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stdio.h>
#include<algorithm>
#include <string>
#include <cstring>
using namespace std;

#define gc getchar
#define pc(x) putchar
#define pi(n) printf("%d",n)
#define pll(n) printf("%lld",n)
#define ps printf(" ")
#define pn printf("\n")
#define rep(i,n) for(i=0;i<n;i++)
#define fu(i,a,n) for(i=a;i<=n;i++)
#define fd(i,n,a) for(i=n;i>=a;i--)
inline int sn()
{
    int n=0;
    int ch=gc();
    while( ch <48 )ch=gc();
    while( ch >47 )
    n = (n<<3)+(n<<1) + ch-'0', ch=gc();
    return n;
}

vector<int> arr(150,0);
vector<int> arr1(150,0);
void partition(int low,int high);
void mergeSort(int low,int mid,int high);
void partition(int low,int high)
{
    int mid;
    if(low<high){
         mid=(low+high)/2;
         partition(low,mid);
         partition(mid+1,high);
         mergeSort(low,mid,high);
    }
}

void mergeSort(int low,int mid,int high)
{

    int i,m,k,l,temp[150],temp1[150];

    l=low;
    i=low;
    m=mid+1;

    while((l<=mid)&&(m<=high)){

         if(arr[l]<=arr[m]){
             temp[i]=arr[l];
             temp1[i]=arr1[l];
             l++;
         }
         else{
             temp[i]=arr[m];
             temp1[i]=arr1[m];
             m++;
         }
         i++;
    }

    if(l>mid){
         for(k=m;k<=high;k++){
             temp[i]=arr[k];
             temp1[i]=arr1[k];
             i++;
         }
    }
    else{
         for(k=l;k<=mid;k++){
             temp[i]=arr[k];
             temp1[i]=arr1[k];
             i++;
         }
    }

    for(k=low;k<=high;k++){
         arr[k]=temp[k];
         arr1[k]=temp1[k];
    }
}

char x[50005][100],s[100],x1[50005][100];
vector<int> y(50005);
vector<int> y1(50005);
int n,i,j,k;

int main()
{
    while(1)
    {
        map<string,int> M;
        n=sn();
        if(n==0) break;
        rep(i,n)
        {
            y[i]=0;
            y1[i]=0;
        }
        rep(i,n)
        {
            scanf("%s",s);
            for(j=0;s[j]!='/';j++)
            {
                x[i][j]=s[j];
            }
            x[i][j]=0;
            j++;
            for(k=j;s[k]!=0;k++)
            {
                y[i]=10*y[i]+(int)(s[k])-48;
            }
            M[x[i]]=i;
        }
        int d=0;
        for(map<string,int>::iterator it = M.begin(); it != M.end(); it++)
        {
            int h=it->second;
            for(j=0;;j++)
            {
                if(j!=0)
                    if(x[h][j-1]==0)
                        break;
                x1[d][j]=x[h][j];
            }
            y1[d]=y[h];
            d++;
        }
        int count;
        vector<int> close(50005,0);
        vector<int> open(50005,0);
        stack<int> s;
        rep(i,n)
        {
            count=0;
            while(!s.empty())
            {
                int top=s.top();
                if(top<y1[i])
                {
                    s.pop();
                    count++;
                }
                else break;
            }
            s.push(y1[i]);
            if(i!=0) close[i-1]=count;
        }
        count=0;
        while(!s.empty())
        {
            int top=s.top();
            if(top>-1)
            {
                s.pop();
                count++;
            }
            else break;
        }
        close[n-1]=count;



        stack<int> s1;
        rep(i,n)
        {
            count=0;
            while(!s1.empty())
            {
                int top=s1.top();
                if(top<y1[n-1-i])
                {
                    s1.pop();
                    count++;
                }
                else break;
            }
            s1.push(y1[n-1-i]);
            if(i!=0)
                open[n-i]=count;
        }
        count=0;
        while(!s1.empty())
        {
            int top=s1.top();
            if(top>-1)
            {
                s1.pop();
                count++;
            }
            else break;
        }
        open[0]=count;

        rep(i,n)
        {
           // printf("%d %d %d\n",i,open[i],close[i]);
            rep(j,open[i]) printf("(");
            printf("%s/%d",x1[i],y1[i]);
            rep(j,close[i]) printf(")");

        }
        pn;



    }

    return 0;
}
