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

mod=998244353

def poly_pow(v,k):
    if k<1:
        return[1]
    if k<2:
        return v
    r=poly_pow(v,k//2)
    r=poly_mul(r,r)
    if k%2:
        r=poly_mul(r,v)
    return[i%mod for i in r]

N=int(input())//2
p=poly_pow([1]*10,N//2)
q=p
if N%2:
    q=poly_mul([1]*10,q)
p=sum(i*i%mod for i in p)%mod
q=sum(i*i%mod for i in q)%mod
print(p*q%mod)