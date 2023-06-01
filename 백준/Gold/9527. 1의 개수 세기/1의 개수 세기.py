def S(x):
 if x==0:return 0
 n=x;c=-1
 while n:n>>=1;c+=1
 return(c*x//2+1)*(2**c==x)or S(2**c)+S(d:=x-2**c)+d
p,q=map(int,input().split())
print(S(q)-S(p-1))