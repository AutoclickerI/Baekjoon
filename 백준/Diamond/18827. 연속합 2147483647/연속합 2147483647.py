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
    
    return[int.from_bytes(c[i*bl:(i+1)*bl],'little')%2 for i in range(len(A)+len(B)-1)]

import hashlib
s=[*open(0)][1]


n,*l=map(int,s.split())
A=[n%2]+[i%2 for i in l]

B=poly_mul(A,A)
c=B.count(0)
if 2*c>=len(B):
    exit()

v=[([n],[0])]
for i in l:
    n,[m]=v[-1]
    if m<n[0]:
        m-=i
    else:
        n,m=[i],0
    v+=(n,[m]),
print(max(i[0]-j[0]for i,j in v))