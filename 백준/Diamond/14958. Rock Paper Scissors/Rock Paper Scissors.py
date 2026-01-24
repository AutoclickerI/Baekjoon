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

N,M=map(int,input().split())
rps=input()
machine=input()[::-1]

*rps_r,=map('R'.__eq__,rps)
*rps_p,=map('P'.__eq__,rps)
*rps_s,=map('S'.__eq__,rps)
*machine_r,=map('R'.__eq__,machine)
*machine_p,=map('P'.__eq__,machine)
*machine_s,=map('S'.__eq__,machine)

w1=poly_mul(rps_r,machine_p)
w2=poly_mul(rps_p,machine_s)
w3=poly_mul(rps_s,machine_r)

*w,=map(sum,zip(w1,w2,w3))
print(max(w[M-1:]))