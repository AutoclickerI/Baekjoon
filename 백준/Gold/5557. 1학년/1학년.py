N,s,*P,e=map(int,open(0).read().split())

v=[0]*21

v[s]=1

for i in P:
    tmp=[0]*21
    for c in range(21):
        if c+i<21:
            tmp[c+i]+=v[c]
        if 0<=c-i:
            tmp[c-i]+=v[c]
    v=tmp
print(v[e])