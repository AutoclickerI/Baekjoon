n,k=map(int,input().split())
r=n*k
s=1
while k>=s<=n:a=k//s;e=min(k//a,n);r+=a*(s+e)*(s-e-1)//2;s=e+1
print(r)