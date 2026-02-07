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

mod=10**9+7
N,K,M=map(int,input().split())
mul=[0]*(N-1-K)+[pow(K+1,-1,mod)]*-~K

def reduce(arr):
    while N<len(arr):
        v=arr.pop()
        l=len(arr)
        for j in range(N):
            arr[l-1-j]=(arr[l-1-j]+v*mul[j])%mod
    return[i%mod for i in arr]

def poly_pow(poly,k):
    if k==0:
        return[1]
    if k==1:
        return poly
    v=poly_pow(poly,k//2)
    r=reduce(poly_mul(v,v))
    if k%2:
        r=reduce(poly_mul(r,poly))
    return r

c=poly_pow([0,1],M)+[0]*N

print(*c[:N])