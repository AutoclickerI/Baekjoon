n,k=map(int,input().split())
e=[1]*n
i=(k-1)%n
while e[i]:e[i]=0;i=(i+k)%n
print(sum(e))