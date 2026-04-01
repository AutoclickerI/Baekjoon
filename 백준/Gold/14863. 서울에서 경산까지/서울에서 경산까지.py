[N,K],*l=[map(int,i.split())for i in open(0)]

v=[-float('inf')]*-~K
v[0]=0

for t1,c1,t2,c2 in l:
    t=[-float('inf')]*-~K
    for i in range(K+1):
        if i+t1<K+1:
            t[i+t1]=max(t[i+t1],v[i]+c1)
        if i+t2<K+1:
            t[i+t2]=max(t[i+t2],v[i]+c2)
    v=t

print(max(v))