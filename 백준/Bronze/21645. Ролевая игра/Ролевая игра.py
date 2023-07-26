n,m,k=map(int,input().split())
print(n*(m//k+min(m,k-1)))