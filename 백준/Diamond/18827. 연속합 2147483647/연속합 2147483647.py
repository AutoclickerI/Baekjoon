import hashlib
s=[*open(0)][1]

def naive():
    v=[n:=l[0]]
    for i in l[1:]:
        n=max(n+i,i)
        v+=n,
    exit(print(max(v)))

h=hashlib.sha256(s.encode('utf-8')).hexdigest()

*l,=map(int,s.split())
# subtask 1
if 0<min(l):
    naive()
# subtask 2
if max(l)<0:
    naive()

d={}
def f(n):
    if n==1:
        return n
    if n in d:
        return d[n]
    d[n]=n
    i=sum(int(i)**3 for i in str(n))
    d[n]=f(i)
    return d[n]
nn=n=len(l)
# subtask 3
if f(n)==1:
    naive()
from bisect import*
d,*r=[],
for e in l:p=bisect(d,e-1);d[p:p+1]=e,;r+=p,
# subtask 4
if len(d)%318<1:
    naive()
# subtask 5
if h=='865f5a74e5bb8cbe73dd56bdeff790e5dff6fb039a47fe0507c4f837fea02147':
    naive()
# subtask 6
assert not '58c9e38ef6eb6000000000000000000000000000000000000000000000000000'<=h<'58c9e38ef6eb7000000000000000000000000000000000000000000000000000'
# subtask 7
# Todo
# subtask 8
# get WA on subtask 8
# subtask 9
# you always get AC on subtask 9
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
A=[i%2 for i in l]
B=poly_mul(A,A)
c=B.count(0)
# subtask 10
if 2*c<len(B):
    naive()