[N],l,r=[[*map(int,i.split())]for i in open(0)]

sc=[-float('inf')]*N+[0]
for j in range(N):
    v=l[j]
    for i in range(N):
        if r[i]<v:
            sc[i]=max(sc[i],sc[i-1]+r[i])
    for i in range(N)[::-1]:
        sc[i]=max(sc[i],sc[i-1])
print(max(sc))