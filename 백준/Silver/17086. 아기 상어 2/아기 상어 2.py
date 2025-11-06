[N,M],*b=[[*map(int,i.split())]for i in open(0)]

l=[]

for y in range(N):
    for x in range(M):
        if b[y][x]:l+=(y,x),

print(max(min(max(abs(y2-y),abs(x2-x))for y,x in l)for y2 in range(N)for x2 in range(M)))