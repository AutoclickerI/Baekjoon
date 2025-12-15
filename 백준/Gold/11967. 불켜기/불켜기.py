[N,M],*l=[map(int,i.split())for i in open(0)]

s={(1,1)}
v={(1,1)}
d={}
for x,y,a,b in l:d[x,y]=d.get((x,y),[]);d[x,y]+=(a,b),

l=[(1,1)]

for i in l:
    y,x=i
    for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
        ny,nx=y+dy,x+dx
        if(ny,nx)in s and(ny,nx)not in v:
            v.add((ny,nx))
            l+=(ny,nx),
    for e in d.get(i,[]):
        s.add(e)
        y,x=e
        for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
            ny,nx=y+dy,x+dx
            if(ny,nx)in v and(y,x)not in v:
                v.add((y,x))
                l+=(y,x),
print(len(s))