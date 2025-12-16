N,L,R,X,*l=map(int,open(c:=0).read().split())

for i in range(2**N):
    t=[]
    mv=float('inf')
    Mv=-L
    s=0
    for v in l:
        if i%2:
            s+=v
            mv=min(mv,v)
            Mv=max(Mv,v)
        i//=2
    c+=L<=s<=R and X<=Mv-mv
print(c)