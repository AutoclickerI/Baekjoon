def pack(P,k):
    ba=bytearray()
    for v in P:
        ba.extend(int(v).to_bytes(k,'little'))
    return int.from_bytes(ba,'little')

def poly_mul_nonneg(A,B):
    maxA=max(A)
    maxB=max(B)
    bl=max(1,0-max(maxA,maxB,maxA*maxB*min(len(A),len(B))).bit_length()//-8)

    a=pack(A,bl)
    b=pack(B,bl)
    c=a*b
    
    c=c.to_bytes((len(A)+len(B)-1)*bl,'little')
    
    return[int.from_bytes(c[i*bl:(i+1)*bl],'little')for i in range(len(A)+len(B)-1)]

def conv1(r,n):
    ret=[]
    s=0
    for i in range(len(r)+n-1):
        if i<len(r):
            s+=r[i]
        if 0<=i-n:
            s-=r[i-n]
        ret+=s,
    return ret

def shift1(r,n):
    ret=[]
    s=0
    for i in range(r+n-1):
        if i<r:
            s+=1
        if 0<=i-n:
            s-=1
        ret+=s,
    return ret

def poly_mul(A,B):
    if[]in[A,B]:
        return[]
    minA=min(A)
    minB=min(B)
    A=[i-minA for i in A]
    B=[i-minB for i in B]
    ret=poly_mul_nonneg(A,B)
    sab=conv1(B,len(A))
    sba=conv1(A,len(B))
    sasb=shift1(len(A),len(B))
    return[i+p*minA+q*minB+r*minA*minB for i,p,q,r in zip(ret,sab,sba,sasb)]

N=int(input())
s1=input()
s2=input()
sign=0
if s1[0]=='~':
    sign^=1
    s1=s1[1:]
if s2[0]=='~':
    sign^=1
    s2=s2[1:]

def group(arr,chunk):
    arr+=[0]*(chunk-1)
    t=[]
    for i in zip(*[iter(arr)]*chunk):
        i=[*i][::-1]
        x=0
        for v in i:
            x*=N
            x+=v
        t+=x,
    return t

def ungroup(arr,chunk):
    t=[]
    for i in arr:
        for j in range(chunk):
            if j==chunk-1:
                t+=i,
            else:
                t+=i%abs(N),
            i-=i%abs(N)
            i//=N
    return t

chunk=32
s1=[ord(i)-33 for i in s1][::-1]
s1=group(s1,chunk)
s2=[ord(i)-33 for i in s2][::-1]
s2=group(s2,chunk)

ret=poly_mul(s1,s2)
ret=ungroup(ret,chunk)

i=0
while i<len(ret):
    over=ret[i]//abs(N)
    ret[i]%=abs(N)
    if over:
        if i==len(ret)-1:
            ret+=0,
        if 0<N:
            ret[i+1]+=over
        else:
            ret[i+1]-=over
    i+=1
while 1<len(ret) and ret[-1]==0:
    ret.pop()
ret=ret[::-1]
if ret==[0]:
    sign=0
print(sign*'~',*[chr(i+33)for i in ret],sep='')