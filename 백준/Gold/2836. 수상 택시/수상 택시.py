[N,M],*l=[map(int,i.split())for i in open(0)]

q=sorted((e,s)for s,e in l if e<s)

if q:
    l,r=q[0]
    for a,b in q[1:]:
        if a<=r:
            if r<b:
                r=b
        else:
            M+=r-l<<1
            l,r=a,b
    M+=r-l<<1

print(M)