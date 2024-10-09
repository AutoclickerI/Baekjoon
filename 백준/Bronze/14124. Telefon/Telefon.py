def f(n):
 p=s=[];i=j
 while i:s+=i%n,;i//=n
 return sum((i!=p)+0*(p:=i)for i in s)
j=int(input())
print(min(range(10,1,-1),key=f))