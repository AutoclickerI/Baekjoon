n,*l=map(int,[*open(0)][1].split())
v=[(n,0)]
for i in l:
    n,m=v[-1]
    if m<n:
        m-=i
    else:
        n,m=i,0
    v+=(n,m),
print(max(i-j for i,j in v))