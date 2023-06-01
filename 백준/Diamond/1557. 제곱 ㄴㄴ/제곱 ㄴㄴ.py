m=6**6
S=[0]*m
S[1]=1
for i in range(1,m):
 for j in range(2*i,m,i):S[j]-=S[i]
def f(n):
 a=0;i=1
 while i*i<=n:a+=S[i]*(n//i**2);i+=1
 return a
s=k=int(input())
e=2*k
while s<=e:
 m=(s+e)//2
 if f(m)<k:s=m+1
 else:e=m-1;a=m
print(a)