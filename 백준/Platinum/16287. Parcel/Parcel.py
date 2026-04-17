import sys
input=sys.stdin.readline

w,n=map(int,input().split())
l=sorted(map(int,input().split()))
K=w+1

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

    return[int.from_bytes(c[i*bl:(i+1)*bl],'little')for i in range(len(A)+len(B)-1)][:K]

if w<sum(l[:4])or sum(l[-4:])<w:
    exit(print('NO'))

mx=min(l[-1],w)

p1=[0]*-~mx
p2=[0]*-~min(mx*2,w)
s3=set()
s4=set()

for x in l:
    if x<=w:
        p1[x]=1
    if x*2<=w:
        p2[x*2]=1
    if x*3<=w:
        s3.add(x*3)
    if x*4<=w:
        s4.add(x*4)

q=poly_mul(p1,p1)

c1=c2=0
s=max(0,w-len(q)+1)
e=min(w,len(q)-1)
for i in range(s,e+1):
    c1+=q[i]*q[w-i]
    if w-i<len(p2):
        c2+=q[i]*p2[w-i]

c3=0
s=max(0,w-len(p2)+1)
e=min(w,len(p2)-1)
for i in range(s,e+1):
    c3+=p2[i]*p2[w-i]

c4=0
for x in l:
    c4+=w-x in s3

c5=w in s4

print('YNEOS'[c1-6*c2+3*c3+8*c4-6*c5<1::2])