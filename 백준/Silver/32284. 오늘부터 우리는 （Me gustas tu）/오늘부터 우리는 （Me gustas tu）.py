N,M,a,b=map(int,open(0).read().split())
t=[''for _ in[0]*N]
for y in range(N):
    for x in range(M):
        if x<b:t[y]+='E'
        elif x>b:t[y]+='W'
        else:t[y]+='NS'[y<a]
for i in t:print(i)