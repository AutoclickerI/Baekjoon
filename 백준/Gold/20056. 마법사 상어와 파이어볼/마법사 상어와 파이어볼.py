[N,M,K],*l=[[*map(int,i.split())]for i in open(0)]
b=[[[]for _ in[0]*N]for _ in[0]*N]
for r,c,m,s,d in l:
    b[r-1][c-1]+=(m,s,d),
for _ in[0]*K:
    t=[[[]for _ in[0]*N]for _ in[0]*N]
    for y in range(N):
        for x in range(N):
            for m,s,d in b[y][x]:
                dy,dx=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)][d]
                t[(y+dy*s)%N][(x+dx*s)%N]+=(m,s,d),
    b=[[[]for _ in[0]*N]for _ in[0]*N]
    for y in range(N):
        for x in range(N):
            if 1<len(t[y][x]):
                mm,ss,dd=zip(*t[y][x])
                mm=sum(mm)//5
                if mm:
                    ss=sum(ss)//len(ss)
                    dd=len({i%2 for i in dd})
                    for d in-1,1,3,5:
                        b[y][x]+=(mm,ss,d-dd),
            else:
                b[y][x]+=t[y][x]
a=0
for y in range(N):
    for x in range(N):
        for m,*_ in b[y][x]:
            a+=m
print(a)