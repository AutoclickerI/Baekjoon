import sys
sys.setrecursionlimit(10**5)

N=int(input())

class segtree:
    def __init__(self,N,l,func):
        self.N=N
        self.tree=[0]*N+l
        
        self.func=func
        
        for i in range(N-1,0,-1):
            self.tree[i]=func(self.tree[i*2],self.tree[i*2+1])

    def update(self,idx,v):
        idx+=self.N
        self.tree[idx]=v
        while idx:=idx//2:
            self.tree[idx]=self.func(self.tree[idx*2],self.tree[idx*2+1])
    
    def get_val(self,l,r):
        l+=self.N;r+=self.N
        ret=None
        while l<r:
            if l%2:
                if ret==None:
                    ret=self.tree[l]
                else:
                    ret=self.func(ret,self.tree[l])
                l+=1
            if r%2:
                r-=1
                if ret==None:
                    ret=self.tree[r]
                else:
                    ret=self.func(ret,self.tree[r])
            l//=2
            r//=2
        return ret

*l,=map(int,input().split())

mintree=segtree(N,l,min)
addtree=segtree(N,l,int.__add__)

def bisect(n,s,e):
    v=s
    while 1<e-s:
        m=s+e>>1
        if n<mintree.get_val(v,m):
            s=m
        else:
            e=m
    return s

maxval=-1
maxidx=None

def recur(s,e):
    global maxval,maxidx
    if s==e:
        return
    minval=mintree.get_val(s,e)
    sumval=addtree.get_val(s,e)
    if maxval<minval*sumval:
        maxval=minval*sumval
        maxidx=s,e
    if s+1==e:
        return
    next_idx=bisect(minval,s,e)
    recur(s,next_idx)
    recur(next_idx+1,e)

recur(0,N)

print(maxval)
print(maxidx[0]+1,maxidx[1])