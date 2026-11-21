n,*r=int(input()),
for i in range(n):
 r=n-i,*r;t=n-i
 while t:r=r[-1:]+r[:-1];t-=1
print(*r)