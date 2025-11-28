from itertools import*
for i in[*open(0)][2::2]:print(+(len(i)<161)and min(sum((i!=j)+(j!=k)+(k!=i)for i,j,k in zip(*x))for x in combinations(i.split(),3)))