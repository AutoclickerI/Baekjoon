n,k=map(int,input().split())
n-=1;k-=1
print(-((n+k>0)and(k<1or(n%k!=0)-n//k*(n%k==0))))