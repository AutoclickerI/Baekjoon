N=int(input())
K=int(input())
s=0;e=10**9
while s<=e:
    m=(s+e)//2
    if K>sum(min(N,m//i)for i in range(1,N+1)):s=m+1
    else:e=m-1
print(s)