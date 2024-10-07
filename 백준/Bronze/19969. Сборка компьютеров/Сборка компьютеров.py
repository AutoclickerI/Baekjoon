a,b,c,d,e,f=map(int,open(x:=0).read().split())
m=min(a,d)
d-=m
n=min(b,e)
e-=n
o=min(c,d+e)
print(x+min(f+m+n+o,a+b+c))