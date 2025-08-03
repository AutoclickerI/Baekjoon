from itertools import*
(K,N),*l=[[*map(int,i.split())]for i in open(0)]
print(sum(sum(v.index(j)<v.index(i)for v in l)%K<1for i,j in combinations(range(1,N+1),2)))