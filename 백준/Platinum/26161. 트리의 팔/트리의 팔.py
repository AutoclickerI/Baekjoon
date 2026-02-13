def pack(P,k):
    ba=bytearray()
    for v in P:
        ba.extend(int(v).to_bytes(k,'little'))
    return int.from_bytes(ba,'little')

def poly_mul(A,B):
    if[]in[A,B]:
        return[]
    if min(min(A),min(B))<0:
        raise ValueError("Not implemented with negative integer.")
    maxA=max(A)
    maxB=max(B)
    bl=max(1,0-max(maxA,maxB,maxA*maxB*min(len(A),len(B))).bit_length()//-8)

    a=pack(A,bl)
    b=pack(B,bl)
    c=a*b
    
    c=c.to_bytes((len(A)+len(B)-1)*bl,'little')
    
    return[int.from_bytes(c[i*bl:(i+1)*bl],'little')for i in range(len(A)+len(B)-1)]

N,R=map(int,input().split())
edges=[[]for _ in[0]*-~N]
for _ in[0]*~-N:
    u,v=map(int,input().split())
    edges[u]+=v,
    edges[v]+=u,

v=[0]*-~N
d=[0]*N

l=[(R,0)]
v[R]=1
for n,c in l:
    f=1
    for e in edges[n]:
        if v[e]<1:
            v[e]=1
            f=0
            l+=(e,c+1),
    d[c]+=f
v=poly_mul(d,d)

s=[0]
for i in v:s+=(s[-1]+i)%(10**9+7),
for _ in[0]*int(input()):
    w,v=map(int,input().split())
    print((s[v+1]-s[w])%(10**9+7))