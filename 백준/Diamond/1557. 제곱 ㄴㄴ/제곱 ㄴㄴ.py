m=6**6
S=[i:=0,1]+[0]*m
while(i:=i+1)<m:
 j=2*i
 while j<m:S[j]-=S[i];j+=i
def f(n,a=0,i=1):
 while i*i<=n:a+=n//i**2*S[i];i+=1
 return a
s=k=int(input())
e=2*k
while s<=e:
 if f(m:=(s+e)//2)<k:s=m+1
 else:e=m-1;a=m
print(a)