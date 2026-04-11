from bisect import*
[N,M],*l=[[*map(int,i.split())]for i in open(0)]
m=10**9
for i in l:
    i.sort()
pt=[0]*N
def fi(n):
    r=0
    for idx,i in enumerate(l):
        while pt[idx]<M and i[pt[idx]]<n:
            pt[idx]+=1
        if pt[idx]==len(i):
            exit(print(m))
        r=max(r,i[pt[idx]]-n)
    return r

for i in sorted(sum(l,[])):
    m=min(m,fi(i))