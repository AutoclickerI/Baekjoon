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
s1=[ord(i)-33 for i in s1]
s2=[ord(i)-33 for i in s2]
ret=poly_mul(s1,s2)[::-1]
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