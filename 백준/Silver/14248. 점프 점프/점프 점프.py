n,*b,s=map(int,open(0).read().split())
l=[s-1]
v=[0]*-~n
v[s-1]=1

for i in l:
    for e in i-b[i],i+b[i]:
        if 0<=e<n and v[e]<1:
            v[e]=1
            l+=e,
print(len(l))