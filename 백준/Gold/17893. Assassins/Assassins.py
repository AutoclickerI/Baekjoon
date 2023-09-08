N,M=map(int,input().split())
prob=[0]*(1<<N)
prob[-1]=1
for _ in[0]*M:
    s,e,p=map(eval,input().split())
    for i in range(1<<N):
        if i&(1<<s-1) and i&(1<<e-1):
            prob[i^(1<<e-1)]+=prob[i]*p
            prob[i]*=1-p
assissin=[0]*N
for i in range(1<<N):
    for j in range(N):
        if i&(1<<j):
            assissin[j]+=prob[i]
print(*assissin)