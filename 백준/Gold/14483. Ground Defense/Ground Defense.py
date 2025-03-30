import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

def update_lazy(s,e,l,r,v,i,idx):
    if e<=l or r<=s:
        return
    if s<=l and r<=e:
        sv,inc=lazy[idx]
        lazy[idx]=sv+v+i*(l-s),inc+i
        return
    if l+1<r:
        m=l+r>>1
        update_lazy(s,e,l,m,v,i,idx*2)
        update_lazy(s,e,m,r,v,i,idx*2+1)
    
def propagate(l,r,idx):
    #print('prapagate',l,r,idx)
    sv,inc=lazy[idx]
    tree[idx]+=sv*(r-l)+inc*(r-l)*(r-l-1)//2
    if l+1<r:
        sv1,inc1=lazy[idx*2]
        lazy[idx*2]=sv1+sv,inc1+inc
        sv2,inc2=lazy[idx*2+1]
        lazy[idx*2+1]=sv2+sv+inc*((l+r)//2-l),inc2+inc
    lazy[idx]=0,0

def get_val(s,e,l,r,idx):
    #print('get_val',s,e,l,r,idx)
    if e<=l or r<=s:
        return 0
    propagate(l,r,idx)
    if s<=l and r<=e:
        return tree[idx]
    m=l+r>>1
    return get_val(s,e,l,m,idx*2)+get_val(s,e,m,r,idx*2+1)

T=int(input())

for _ in[0]*T:
    M,N=map(int,input().split())
    tree=[0]*4*-~N
    lazy=[(0,0)]*4*-~N
    for _ in[0]*M:
        q,*l=input().split()
        if q=='U':
            i,s,a,d=map(int,l[1:])
            if l[0]=='E':
                update_lazy(i-1,i+d-1,0,N,s,a,1)
            else:
                update_lazy(i-d,i,0,N,s+(d-1)*a,-a,1)
        else:
            print(get_val(int(l[0])-1,int(l[0]),0,N,1))