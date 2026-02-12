import sys

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

mod=1000003

def fast_ints():
    x=0
    for v in sys.stdin.buffer.read():
        if v<=32:
            yield x
            x=0
        else:
            x=x*10+v-48

def poly_add(acc,poly):
    L=min(k+1,len(poly))
    acc+=[0]*(L-len(acc))
    for i in range(L):
        acc[i]=(acc[i]+poly[i])%mod
    return acc

it=fast_ints()
n=next(it)
k=next(it)
r=next(it)

if n<k:
    exit(print(0))
    
cnt=[0]*r
for _ in range(n):
    a=next(it)
    cnt[a%r]+=1

F=[[1]]+[[]for _ in range(r-1)]

for x in range(r):
    c=cnt[x]
    if c<1:
        continue

    d=min(c,k)

    H=[-~d*[0]for _ in range(r)]
    C=1
    for i in range(d+1):
        H[x*i%r][i]=C
        if i<d:
            C=C*(c-i)*pow(i+1,-1,mod)%mod

    nn=[]
    for s in range(r):
        if H[s]:nn+=s,

    nF=[[]for _ in range(r)]
    for t in range(r):
        if not F[t]:
            continue
        for s in nn:
            u=(t+s)%r
            nF[u]=poly_add(nF[u],poly_mul(F[t],H[s]))
    F=nF

print(F[0][k]%mod*(k<len(F[0])))