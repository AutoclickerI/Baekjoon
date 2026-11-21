n,k=map(int,input().split())
r=s=1
while k>=s<=n:a=k//s;e=min(k//a,n);r+=a*(s+e)*(s+~e);s=e+1
print(r//2+n*k)