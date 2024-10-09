n,k,*a=map(int,open(0).read().split())
p=[0]*n*3
s=p[:]
for i in range(n):p[i+1]=a[i]+p[i]
for i in range(n,0,-1):s[i]=s[i+1]+a[i-1]
print(max(p[max(0,i-k)]+s[min(n+1,i+k+2)]+a[i]*(1+min(k,n+~i)+min(k,i))for i in range(n)))