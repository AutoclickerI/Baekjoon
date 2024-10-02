n,*a=map(int,open(0).read().split())
m=round(sum(a)/n)
v=[0,0]
for x in a:f=x>m;v[f]+=(x-m)*(2*f-1)
print(max(v))