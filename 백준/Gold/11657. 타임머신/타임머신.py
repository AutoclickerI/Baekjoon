(N,M),*l=[[*map(int,i.split())]for i in open(0)]
cost=[float('inf')]*-~N
cost[1]=0
f=0
for i in range(N):
    for a,b,c in l:
        if cost[a]+c<cost[b]:
            cost[b]=cost[a]+c
            f|=i==N-1
if f:
    print(-1)
else:
    for i in cost[2:]:
        print(i if i!=float('inf')else-1)