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

n,p=map(int,input().split())
s=input()
R,B,Y=[[*map(i.__eq__,s)]for i in'RBY']
Rv=poly_mul(R*2,R[::-1])
Bv=poly_mul(B*2,B[::-1])
Yv=poly_mul(Y*2,Y[::-1])
Sv=[len(s)-i-j-k for i,j,k in zip(Rv,Bv,Yv)][len(s):-len(s)]
ss=sorted((Sv[i],~i)for i in range(len(s)-1))
d={}
for v,i in ss:
    d[v]=-i
print(d[ss[p-1][0]])