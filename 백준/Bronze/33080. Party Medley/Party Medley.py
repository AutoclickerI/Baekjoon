from itertools import*
n,d,*l=map(int,open(0).read().split())
l=[sum(i)for i in combinations(l,3)if max(i)-min(i)<=d]
print(*l and[len(l),max(l+[0])]or[-1])