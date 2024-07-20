N,M=map(int,input().split())
*d,=map(int,input().split())
k=eval('[*map(int,input().split())],'*M)
m=1e18
from itertools import permutations
for order in permutations(range(M),M):
    study=0
    valid=[-1]*-~N
    t=0
    for i in order:
        _,*l=k[i]
        for j in l:
            if valid[j]<t:
                valid[j]=t+d[j-1]-1
                study+=1
        t+=1
    m=min(study,m)
print(m) 