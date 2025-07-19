n,x,*A=map(int,open(t:=0).read().split())
while A:
 a,b,*A=A
 if x<abs(a-b):t+=A.pop(0)
 else:t+=max(a,b)
print(t)