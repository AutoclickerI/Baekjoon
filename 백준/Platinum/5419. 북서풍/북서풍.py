def update(idx):
    idx+=N
    tree[idx]+=1
    while 1<idx:
        idx//=2
        tree[idx]=tree[idx*2]+tree[idx*2+1]

def get_val(l,r):
    l+=N
    r+=N
    ret=0
    while l<r:
        if l%2:
            ret+=tree[l]
            l+=1
        if r%2:
            r-=1
            ret+=tree[r]
        l//=2
        r//=2
    return ret

for T in[0]*int(input()):
    l=sorted([[*map(int,input().split())]for _ in[0]*int(input())],key=lambda s:(s[0],-s[1]))
    sl=sorted({j for i,j in l})
    N=len(sl)
    compress={}
    for i in range(N):
        compress[sl[i]]=i
    
    tree=[0]*2*N
    
    ans=0
    
    for x,y in l:
        ans+=get_val(compress[y],N)
        update(compress[y])
    print(ans)