[N,M],*l=[map(int,i.split())for i in open(0)]

q=[]
for v,c,k in l:
    i=1
    while i<=k:
        q+=(v*i,c*i),
        k-=i
        i<<=1
    if k:
        q+=(v*k,c*k),

f=[0]*-~M
for v,c in q:
    for i in range(M,0,-1):
        if 0<=i-v:
            f[i]=max(f[i],f[i-v]+c)
print(f[-1])