N,*l=map(int,input().split())

v={(0,0)}
ans=0

def backtrack(y,x,p,c):
    global ans
    if c==N:
        ans+=p
        return
    for i in range(4):
        dy,dx=[(0,1),(0,-1),(-1,0),(1,0)][i]
        ny,nx=y+dy,x+dx
        if(ny,nx)not in v:
            v.add((ny,nx))
            backtrack(ny,nx,p*l[i],c+1)
            v.remove((ny,nx))

backtrack(0,0,1,0)

print(ans/100**N)