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

m=10**6+1
A=[1]*m
for i in range(2,m):
    if A[i]:
        A[2*i::i]=[0]*len(range(2*i,m,i))

A[:3]=0,0,0
B=[0]*m
for i in range(m//2):
    B[i*2]=A[i]
B[4]=1

v=poly_mul(A,B)

for i in[*open(0)][1:]:
    print(v[int(i)])