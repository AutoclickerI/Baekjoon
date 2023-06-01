m=6**8
S=[0,1]+[0]*m
for i in range(1,m):
 for j in range(2*i,m,i):S[j]-=S[i]
s=k=int(input())
e=4*k
def f(n,a=0,i=1):
 while i*i<=n:a+=n//i**2*S[i];i+=1
 return n-a
while s<=e:
 if f(m:=(s+e)//2)<k:s=m+1
 else:e=m-1;a=m
print(a)