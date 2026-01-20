m=500001
N,*l=map(int,open(0).read().split())

d=[-9e9]*m
d[0]=0

for v in l:
    t=d[:]
    for i in range(m):
        if i+v<m:
            t[i+v]=max(t[i+v],d[i])
        if 0<=i-v:
            t[i-v]=max(t[i-v],d[i]+v)
        else:
            t[v-i]=max(t[v-i],d[i]+i)
    d=t
print(-(d[0]<1)or d[0])