_,*l=map(str.split,open(0))
N=len(l)
v=[N*[-float('inf')]for _ in[0]*N]
v[0][0]=int(l[0][0])
from heapq import*
hq=[(v[0][0],0,0)]
R=(0,1)
D=(1,0)
def cal(a,op,b):
    b=int(b)
    if op=='+':
        return a+b
    if op=='-':
        return a-b
    if op=='*':
        return a*b
while hq:
    n,y,x=heappop(hq)
    if n<v[y][x]:
        continue
    for mv in[(R,R),(R,D),(D,R),(D,D)]:
        yy=y
        xx=x
        st=[]
        for dy,dx in mv:
            ny,nx=yy+dy,xx+dx
            if 0<=ny<N and 0<=nx<N:
                st+=l[ny][nx],
                yy=ny
                xx=nx
            else:
                break
        else:
            cv=cal(n,*st)
            if v[yy][xx]<cv:
                v[yy][xx]=cv
                heappush(hq,(cv,yy,xx))
print(v[-1][-1])
v=[N*[float('inf')]for _ in[0]*N]
v[0][0]=int(l[0][0])
hq=[(-v[0][0],0,0)]
while hq:
    n,y,x=heappop(hq)
    n=-n
    if v[y][x]<n:
        continue
    for mv in[(R,R),(R,D),(D,R),(D,D)]:
        yy=y
        xx=x
        st=[]
        for dy,dx in mv:
            ny,nx=yy+dy,xx+dx
            if 0<=ny<N and 0<=nx<N:
                st+=l[ny][nx],
                yy=ny
                xx=nx
            else:
                break
        else:
            cv=cal(n,*st)
            if cv<v[yy][xx]:
                v[yy][xx]=cv
                heappush(hq,(-cv,yy,xx))
print(v[-1][-1])