[N,C],[M],*l=[[*map(int,i.split())]for i in open(0)]
l.sort()
z=[]
a=0
for s,e,n in l:
    tmp=[]
    aaa=0
    for c,v in z:
        if c<=s:
            a+=v
        else:
            tmp+=(c,v),
            aaa+=v
    tmp+=(e,n),
    aaa+=n
    tmp.sort()
    while C<aaa:
        c,v=tmp.pop()
        aaa-=v
        if aaa<=C:
            tmp+=(c,C-aaa),
            break
    z=tmp
print(a+sum(j for i,j in z))