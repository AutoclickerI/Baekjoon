a,b,n,k=map(int,input().split())
k-=1
k//=n
print(k//b+1,k%b+1)