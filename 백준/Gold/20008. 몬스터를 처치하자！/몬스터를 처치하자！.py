N,H=map(int,input().split())
s=[[*map(int,input().split())]for _ in[0]*N]
t=0
l=[[[0]*N,H]]
f=1
while f:
    z=[]
    for d,h in l:
        v=1
        for i in range(N):
            if d[i]<=t:
                x=d[:]
                x[i]=t+s[i][0]
                z+=[x,h-s[i][1]],
                f&=0<h-s[i][1]
                v=0
        if v:
            z+=[d,h],
    l=z
    t+=1
print(t)