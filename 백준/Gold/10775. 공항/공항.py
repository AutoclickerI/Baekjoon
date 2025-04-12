G,_,*l=map(int,open(0))

tree=[0]*G+[1]*G

for i in range(G-1,0,-1):
    tree[i]=tree[i*2]+tree[i*2+1]

def update(idx,v):
    idx+=G
    tree[idx]=v
    while 1<idx:
        idx//=2
        tree[idx]=tree[idx*2]+tree[idx*2+1]

def get_val(l,r):
    l+=G
    r+=G
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

def bisect(e,v):
    s=0
    while 1<e-s:
        m=e+s>>1
        if get_val(0,m)==v:
            e=m
        else:
            s=m
    return s
            

cnt=0
for i in l:
    v=get_val(0,i)
    if v<1:
        break
    cnt+=1
    update(bisect(i,v),0)

print(cnt)