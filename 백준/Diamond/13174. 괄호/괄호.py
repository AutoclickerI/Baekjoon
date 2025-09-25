n,k=map(int,input().split())
i=r=p=0;c=1
while i*2<=n:r+=pow(k,n-i,M:=10**9+7)*(c-p);p=c;c=c*(i-n)*pow(~i,-1,M)%M;i+=1
print(r%M)