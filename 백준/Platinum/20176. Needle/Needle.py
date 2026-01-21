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

_,a,_,b,_,c=[[*map(int,i.split())]for i in open(0)]

A=[0]*60001
C=[0]*60001

for i in a:
    A[i+30000]=1
for i in c:
    C[i+30000]=1

v=poly_mul(A,C)
B={i*2+60000 for i in b}
r=0
for i in range(1200001):
    if i in B:r+=v[i]
print(r)