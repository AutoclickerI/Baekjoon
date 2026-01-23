[N,M],*l=[map(int,i.split())for i in open(0)]
_,*l=zip(*l)
v=[0]*-~N
d=[{}for _ in v]
cnt=0
for i in l:
    cnt+=1
    t=v[:]
    dt=[{**i}for i in d]
    for j in range(1,N+1):
        for k in range(j):
            n=v[j-k-1]+i[k]
            if t[j]<n:
                t[j]=n
                dt[j]={**d[j-k-1]}|{cnt:k}
    v=t
    d=dt
ii=v.index(max(v))
print(v[ii])
for i in range(M):
    print(d[ii].get(i+1,-1)+1)