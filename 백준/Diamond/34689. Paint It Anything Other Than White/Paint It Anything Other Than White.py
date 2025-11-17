import sys
input=sys.stdin.readline

leaf={'K':(1,1,1,1,1,1,1,1,1,1),
      'R':(1,1,1,0,0,0,1,1,1,1),
      'G':(1,1,1,1,1,1,0,0,0,1),
      'B':(0,0,0,1,1,1,1,1,1,1),
      'Y':(1,1,1,0,0,0,0,0,0,1),
      'C':(0,0,0,1,1,1,0,0,0,1),
      'P':(0,0,0,0,0,0,1,1,1,1),
      'W':(0,0,0,0,0,0,0,0,0,1)}

def mergeLR(a,b,c,d,e,f,cnt1,cnt2):
    na=a+d*(a==cnt1)
    nc=f+c*(f==cnt2)
    return na,max(b,e,c+d,na,nc),nc

def merge(a,b):
    cnta=a[9];cntb=b[9]
    m1,m2,m3=mergeLR(a[0],a[1],a[2],b[0],b[1],b[2],cnta,cntb)
    m4,m5,m6=mergeLR(a[3],a[4],a[5],b[3],b[4],b[5],cnta,cntb)
    m7,m8,m9=mergeLR(a[6],a[7],a[8],b[6],b[7],b[8],cnta,cntb)
    return m1,m2,m3,m4,m5,m6,m7,m8,m9,cnta+cntb

N,K=map(int,input().split())
tree=[leaf['W']]*2*N

for i in range(N-1,0,-1):
    tree[i]=merge(tree[i*2],tree[i*2|1])

def update(idx,v):
    idx+=N
    tree[idx]=v
    while 1<idx:
        idx//=2
        tree[idx]=merge(tree[idx*2],tree[idx*2|1])

def getval(l,r):
    l+=N
    r+=N
    left=None
    right=None
    while l<r:
        if l&1:
            if left==None:
                left=tree[l]
            else:
                left=merge(left,tree[l])
            l+=1
        if r&1:
            r-=1
            if right==None:
                right=tree[r]
            else:
                right=merge(tree[r],right)
        l//=2
        r//=2
    if right==None:
        return left
    if left==None:
        return right
    return merge(left,right)
out=[]
for _ in[0]*K:
    Q,i,x=input().split()
    if Q=='U':
        update(int(i)-1,leaf[x])
    else:
        s,e=map(int,[i,x])
        print(max(getval(s-1,e)[1::3]))