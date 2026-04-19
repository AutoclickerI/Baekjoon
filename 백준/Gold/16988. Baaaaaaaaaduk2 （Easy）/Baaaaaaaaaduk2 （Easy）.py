[N,M],*b=[[*map(int,i.split())]for i in open(0)]

v=[M*[0]for _ in[0]*N]

d={}
dc={}
cnt=0

for y in range(N):
    for x in range(M):
        if v[y][x]<1 and b[y][x]==2:
            cnt+=1
            v[y][x]=cnt
            l=[(y,x)]
            d[cnt]=set()
            for yy,xx in l:
                for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                    ny,nx=yy+dy,xx+dx
                    if 0<=ny<N and 0<=nx<M:
                        if v[ny][nx]<1 and b[ny][nx]==2:
                            l+=(ny,nx),
                            v[ny][nx]=cnt
                        if b[ny][nx]==0:
                            d[cnt].add((ny,nx))
            dc[cnt]=len(l)

rmap={}
r=0
for i in dc:
    if len(d[i])<3:
        d[i]=(*sorted(d[i]),)
        rmap[d[i]]=rmap.get(d[i],0)+dc[i]

s1=sorted(rmap[i]for i in rmap if len(i)<2)
if s1:
    r=sum(s1[-2:])
for i in rmap:
    if 1<len(i):
        r=max(r,rmap.get(i[:1],0)+rmap.get(i[1:],0)+rmap[i])
print(r)