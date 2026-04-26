N,*l=map(int,open(0))

S=1
while S<N:
    S*=2

t=[0]*2*S
t[S:S+N]=[1]*N

for i in range(S-1,0,-1):
    t[i]=t[i<<1]+t[i<<1|1]

def update(x):
    x+=S
    t[x]=0
    while 1<x:
        x>>=1
        t[x]=t[x<<1]+t[x<<1|1]

def kth(k):
    i=1
    while i<S:
        if k<=t[i<<1]:
            i=i<<1
        else:
            k-=t[i<<1]
            i=i<<1|1
    return i-S

r=[0]*N

for i,v in enumerate(l,1):
    x=kth(v+1)
    r[x]=i
    update(x)

print(*r)