[N],*l=[[*map(int,i.split())]for i in open(0)]

m=0

def backtracking(i):
    global m
    if i==N:
        m=max(m,sum(i<1 for i,j in l))
        return
    if l[i][0]<1:
        backtracking(i+1)
        return
    f=1
    for j in range(N):
        if j==i:continue
        if l[j][0]<1:continue
        l[i][0]-=l[j][1]
        l[j][0]-=l[i][1]
        backtracking(i+1)
        l[i][0]+=l[j][1]
        l[j][0]+=l[i][1]
        f=0
    if f:
        backtracking(i+1)
backtracking(0)
print(m)