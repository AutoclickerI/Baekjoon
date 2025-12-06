[N],r,*l=[[*map(int,i.split())]for i in open(0)]

v=float('inf')
rra=[]
def backtrack(i,x,c,rr):
    global v,rra
    if all(map(int.__le__,r,x)):
        if c<v:
            v=c
            rra=rr
        return
    if i==N:
        return
    for j in 0,1,2,3:
        x[j]+=l[i][j]
    backtrack(i+1,x,c+l[i][-1],rr+[i+1])
    for j in 0,1,2,3:
        x[j]-=l[i][j]
    backtrack(i+1,x,c,rr)
backtrack(0,[0,0,0,0],0,[])
if v==float('inf'):
    print(-1)
else:
    print(v)
    print(*rra)