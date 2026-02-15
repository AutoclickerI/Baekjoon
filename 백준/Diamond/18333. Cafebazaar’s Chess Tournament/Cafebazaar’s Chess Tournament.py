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

[N],*l=[map(int,i.split())for i in open(0)]

o=[0]*-~N
e=o[:]
for p,q in l:
    o[p]+=1
    e[q]+=1

A=[0]*-~N
b=0
A[0]=1
for i in e:b+=i;A[b]|=0<i

B=[0]*-~N
r=0
B[0]=1
for i in o:r+=i;B[r]|=0<i
print(sum(0<i for i in poly_mul(A,B)))