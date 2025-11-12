N=int(input())
W=int(input())

l=[(0,1,1,N,N,[])] #cost, y1,x1,y2,x2

for _ in[0]*W:
    y,x=map(int,input().split())
    tmp={}
    hi={}
    for cost,y1,x1,y2,x2,hist in l:
        vv=cost+abs(y1-y)+abs(x1-x)
        if vv<tmp.get((y,x,y2,x2),float('inf')):
            tmp[y,x,y2,x2]=vv
            hi[y,x,y2,x2]=hist+[1]
        vv=cost+abs(y2-y)+abs(x2-x)
        if vv<tmp.get((y1,x1,y,x),float('inf')):
            tmp[y1,x1,y,x]=vv
            hi[y1,x1,y,x]=hist+[2]
    ttmp=[]
    for i in tmp:
        ttmp+=(tmp[i],*i,hi[i]),
    ttmp.sort()
    cost,*x,hist=ttmp[0]
    l=[]
    for c,*z,hist in ttmp:
        if c<=cost+sum(abs(i-j)for i,j in zip(x,z)):
            l+=(c,*z,hist),

        
c,*_,l=l[0]
print(c)
for i in l:print(i)