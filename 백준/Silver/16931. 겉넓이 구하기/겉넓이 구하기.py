[N,M],*b=[[*map(int,i.split())]for i in open(0)]
s=sum(sum(i)for i in b)*6
for y in range(N):
    for x in range(M):
        s-=b[y][x]*2-2
for y in range(N-1):
    for x in range(M):
        s-=min(b[y][x],b[y+1][x])*2
for y in range(N):
    for x in range(M-1):
        s-=min(b[y][x],b[y][x+1])*2
print(s)