n,x,*A=map(int,open(t:=0).read().split())
while A:a,b,*A=A;t+=max(a,b)*(abs(a-b)<=x)or A.pop(0)
print(t)