A,B=open(0)

d={}
c=0
for i in A[:-1]:
    c+=(i=='(')*2-1
    if c<0:break
    d[c]=d.get(c,0)+1
z=l=a=0
for i in B:
    z-=(i==')')*2-1
    l=min(l,z)
    if z==l:
        a+=d.get(-z,0)
print(a)