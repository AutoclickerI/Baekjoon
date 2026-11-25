import math

[N],A,[Q],*l=[[*map(int,i.split())]for i in open(0)]

blk=math.isqrt(N)

K=[a.bit_length()-1 for a in A]
O=sorted(range(N),key=A.__getitem__)
V=[A[i]for i in O]
R=[0]*N
for p,i in enumerate(O):R[i]=p
st=[0]*30
for p in range(N-1,-1,-1):st[K[O[p]]]=p

S=[0]*30
B=[[0]*(32**(4-i)+1)for i in range(4)]
B0,B1,B2,B3=B

def push(i):
    S[K[i]]+=A[i]
    p=R[i]
    w=p>>5
    if not B0[w]:
        x=w>>5
        if not B1[x]:
            y=x>>5
            if not B2[y]:B3[0]|=1<<y
            B2[y]|=1<<(x&31)
        B1[x]|=1<<(w&31)
    B0[w]|=1<<(p&31)

def pop(i):
    S[K[i]]-=A[i]
    p=R[i]
    w=p>>5
    B0[w]^=1<<(p&31)
    if not B0[w]:
        x=w>>5
        B1[x]^=1<<(w&31)
        if not B1[x]:
            y=x>>5
            B2[y]^=1<<(x&31)
            if not B2[y]:B3[0]^=1<<y

def succ(p):
    h=0
    while not B[h][p>>5]>>(p&31):
        p=(p>>5)+1
        h+=1
    m=B[h][p>>5]>>(p&31)
    p+=(m&-m).bit_length()-1
    while h:
        h-=1
        m=B[h][p]
        p=p<<5|(m&-m).bit_length()-1
    return p

ps=pe=0
d={}
for s,e in sorted(l,key=lambda i:(i[0]//blk,i[1])):
    s-=1
    while pe<e:
        push(pe)
        pe+=1
    while e<pe:
        pe-=1
        pop(pe)
    while ps<s:
        pop(ps)
        ps+=1
    while s<ps:
        ps-=1
        push(ps)
    r=0
    for k in range(30):
        if S[k]:
            if r+2<2<<k and r+1<V[succ(st[k])]:break
            r+=S[k]
    d[s+1,e]=r+1

for s,e in l:print(d[s,e])