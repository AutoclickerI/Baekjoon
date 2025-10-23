n,k=map(int,input().split())
from itertools import*
l=sorted({tuple(j for j in i if j)for i in product((0,1,2,3),repeat=n) if sum(i)==n})
k-=1
if k<len(l):
    print(*l[k],sep='+')
else:
    print(-1)