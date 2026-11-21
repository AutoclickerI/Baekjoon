n,m,a,k=map(int,input().split())
k-=a
print(min(n,1-k),1-k//m)