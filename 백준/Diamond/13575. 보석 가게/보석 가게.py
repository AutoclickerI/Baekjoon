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

def vec_pow(v,k):
    if k<2:
        return v
    z=vec_pow(v,k//2)
    z=[0<i for i in poly_mul(z,z)]
    if k%2:
        z=[0<i for i in poly_mul(z,v)]
    return z

N,K,*l=map(int,open(0).read().split())

v=[0]*1001
for i in l:v[i]=1

z=vec_pow(v,K)

for i,v in enumerate(z):
    if v:print(i)