[N,M,H],*l=[map(int,i.split())for i in open(0)]
v=[0]*-~H
v[0]=1
for i in l:
    t=v[:]
    for c in i:
        for j in range(H+1-c):
            t[j+c]+=v[j]
    v=t
print(v[-1]%10007)