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

N,K=map(int,input().split())
s=input()
if K==1:
    exit(print(0))
if K==2:
    exit(print(+all(i!=j for i,j in zip(s,s[1:]))))
m=float('inf')
B=[1]*K
for c in'QAZWSXEDCRFVTGBYHNUJMIKOLP':
    A=[i!=c for i in s]
    v=poly_mul(A,B)[K-1:1-K]
    m=min(m,min(v))
print(m)