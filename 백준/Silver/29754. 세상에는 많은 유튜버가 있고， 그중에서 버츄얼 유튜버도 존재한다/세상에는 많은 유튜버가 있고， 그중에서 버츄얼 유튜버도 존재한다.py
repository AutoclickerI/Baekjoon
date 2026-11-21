N,M=map(int,input().split())
M-=1
vtuber={}
for _ in[0]*N:
    a,b,c,d=input().split()
    b=int(b)-1
    p,q=map(int,c.split(':'))
    r,s=map(int,d.split(':'))
    t=(r-p)*60+s-q
    nd=vtuber.get(a,{'week':{},'time':{}})
    nd['week'][b//7]=nd['week'].get(b//7,0)+1
    nd['time'][b//7]=nd['time'].get(b//7,0)+t
    vtuber[a]=nd
ans=[]
for i in vtuber:
    nd=vtuber[i]
    if {*nd['week']}=={*range(M//7+1)} and all(j>4 for j in nd['week'].values()) and all(j>3599 for j in nd['time'].values()):
        ans+=i,
for i in(sorted(ans)or[-1]):print(i)