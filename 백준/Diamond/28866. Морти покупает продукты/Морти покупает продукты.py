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

def poly_pow(r,k):
    if k<2:
        return r
    rr=poly_pow(r,k//2)
    rr=[i%786433 for i in poly_mul(rr,rr)]
    if k%2:
        rr=poly_mul(r,rr)
    return[i%786433 for i in rr][:50001]

[N,K,Q],v,*l=[map(int,i.split())for i in open(0)]
A=[0]*50001
for i in v:A[i]+=1
v=poly_pow(A,K)
s=[0]
for i in v:s+=s[-1]+i,
for m,M in l:print((s[M+1]-s[m])%786433)