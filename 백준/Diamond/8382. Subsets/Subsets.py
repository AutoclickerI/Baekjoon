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
    
    return[int.from_bytes(c[i*bl:(i+1)*bl],'little')%m for i in range(len(A)+len(B)-1)][:k+1]

def poly_pow(v,p):
    if p<2:
        return v
    r=poly_pow(v,p//2)
    r=poly_mul(r,r)
    if p%2:
        r=poly_mul(r,v)
    return[i%m for i in r]

n,m,k,x=map(int,input().split())
if k<1:
    print(1)
elif n<k:
    print(0)
else:
    cnt=[]
    r=1
    while U:=n//r:
        r*=x
        V=n//r
        cnt+=U-U//x-V+V//x,
    A0=[1]
    A1=[1,1][:k+1]
    Fs=[A1]

    p2=A0
    p1=A1
    for L in range(2,len(cnt)+1):
        t=[0]*-~min(k,L)
        for j in range(min(k,L)+1):
            v=p1[j]if j<len(p1)else 0
            if 0<j and(j-1)<len(p2):
                v+=p2[j-1]
            t[j]=v%m
        Fs+=t,
        p2,p1=p1,t
    r=[1]
    for i in range(len(cnt)):
        c=cnt[i]
        if c<=0:
            continue
        r=poly_mul(r,poly_pow(Fs[i],c))

    print(r[k]if k<len(r)else 0)