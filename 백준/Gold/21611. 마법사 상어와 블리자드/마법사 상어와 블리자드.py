N,M=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]
y=x=N//2
d=0
l=[]
f=0
v=1
try:
    while 1:
        dy,dx=[(0,-1),(1,0),(0,1),(-1,0)][d%4]
        for _ in[0]*v:
            y+=dy;x+=dx
            l+=b[y][x],
        d=d+1&3
        v=v+f
        f^=1
except:
    l=l[:N*N-1]
while l and l[-1]<1:l.pop()

ds=[[0],[2],[4],[6]]
v=[9,11,13,15]
for i in range(4):
    for _ in[0]*49:
        ds[i]+=ds[i][-1]+v[i],
        v[i]+=8
p=[0,0,0]
ds=ds[3],ds[1],ds[0],ds[2]

for _ in[0]*M:
    d,s=map(int,input().split())
    for i in ds[d-1][:s]:
        if i<len(l):l[i]=0
    *l,=filter(int,l)
    f=1
    while f:
        f=0
        nl=[]
        if l:
            t=[l[0]]
            for i in l[1:]:
                if i==t[0]:
                    t+=i,
                else:
                    if 3<len(t):
                        p[t[0]-1]+=len(t)
                        f=1
                    else:
                        nl+=t
                    t=[i]
            if 3<len(t):
                p[i-1]+=len(t)
                f=1
            else:
                nl+=t
        l=nl
    nl=[]
    if l:
        t=[l[0]]
        for i in l[1:]:
            if i==t[0]:
                t+=i,
            else:
                nl+=len(t),t[0]
                t=[i]
        nl+=len(t),i
    l=nl[:N*N-1]
one,two,three=p
print(one+2*two+3*three)