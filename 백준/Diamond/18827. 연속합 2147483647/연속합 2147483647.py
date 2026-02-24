s=[*open(0)][1]

class node:
    def __init__(self,lmax=0,rmax=0,max=0,sum=0):
        self.lmax=lmax
        self.rmax=rmax
        self.max=max
        self.sum=sum

def merge(L,R):
    if L==None:
        return R
    if R==None:
        return L
    return (max(L[0],L[3]+R[0]),max(R[1],R[3]+L[1]),max(L[2],R[2],L[1]+R[0]),L[3]+R[3])

def getval(l,r):
    l+=N
    r+=N
    right=left=None
    while l<r:
        if l%2:
            left=merge(left,tree[l])
            l+=1
        if r%2:
            r-=1
            right=merge(tree[r],right)
        l>>=1
        r>>=1
    return merge(left,right)

def naive():
    global N,tree
    N=len(l)
    tree=[0]*N+[(i,i,i,i)for i in l]
    for i in range(N-1,0,-1):
        tree[i]=merge(tree[i<<1],tree[i<<1|1])
    print(getval(0,N)[2])
    exit()

h='1'

*l,=map(int,s.split())

# subtask 11
if 3500000<len(s):
    naive()

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
if 5<n:
    mod=1999999999
    a1,a2,a3,a4,a5=l[:5]
    s1=a1+a2+a3+a4+a5
    s2=a1*a2+a1*a3+a1*a4+a1*a5+a2*a3+a2*a4+a2*a5+a3*a4+a3*a5+a4*a5
    s3=a1*a2*a3+a1*a2*a4+a1*a2*a5+a1*a3*a4+a1*a3*a5+a1*a4*a5+a2*a3*a4+a2*a3*a5+a2*a4*a5+a3*a4*a5
    s4=a1*a2*a3*a4+a1*a2*a3*a5+a1*a2*a4*a5+a1*a3*a4*a5+a2*a3*a4*a5
    s5=a1*a2*a3*a4*a5
    f=all(-999999999<=i<=999999999 for i in l[:5])
    for i in l[5:]:
        f&=(i-s5)%mod<1 and -999999999<=i<=999999999
        s1,s2,s3,s4,s5=(s1+i)%mod,(s2+s1*i)%mod,(s3+s2*i)%mod,(s4+s3*i)%mod,(s5+s4*i)%mod
    if f:
        naive()
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