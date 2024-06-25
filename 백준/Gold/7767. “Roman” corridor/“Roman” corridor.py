def to_roman(n):
    s=''
    while n>999:
        s+='M'
        n-=1000
    if n>899:
        s+='CM'
        n-=900
    if n>499:
        s+='D'
        n-=500
    if n>399:
        s+='CD'
        n-=400
    while n>99:
        s+='C'
        n-=100
    if n>89:
        s+='XC'
        n-=90
    if n>49:
        s+='L'
        n-=50
    if n>39:
        s+='XL'
        n-=40
    while n>9:
        s+='X'
        n-=10
    if n>8:
        s+='IX'
        n-=9
    if n>4:
        s+='V'
        n-=5
    if n>3:
        s+='IV'
        n-=4
    s+='I'*n
    return s

from heapq import*

def to_int(s):
    d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    return sum(d[i]for i in s)-2*sum(d[i]for i,j in zip(s,s[1:])if d[i]<d[j])

def valid(s):
    return s==to_roman(to_int(s))

N,M=map(int,input().split())
b=eval('input(),'*N)
v=eval('[1e9]*M,'*N)
hq=[]
for i in range(N):
    n=to_int(b[i][0])
    hq+=(n,(i,0)),
    v[i][0]=n
heapify(hq)
visited={}
while hq:
    s,(y,x)=heappop(hq)
    if (s,y,x)in visited:
        continue
    visited[s,y,x]=1
    if 5000<s:
        break
    for dy,dx in(0,1),(0,-1),(-1,0),(1,0):
        r=to_roman(s)
        if 0<=y+dy<N and 0<=x+dx<M and valid(r+b[y+dy][x+dx]):
            i=to_int(r+b[y+dy][x+dx])
            if i<v[y+dy][x+dx]:
                v[y+dy][x+dx]=i
            heappush(hq,(i,(y+dy,x+dx)))

m=min(i[-1]for i in v)
if m==1e9:
    print('NO')
else:
    print(to_roman(m))