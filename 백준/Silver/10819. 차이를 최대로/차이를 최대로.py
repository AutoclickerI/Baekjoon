from itertools import*
print(max(sum(abs(j-k)for j,k in zip(i,i[1:]))for i in permutations(map(int,[*open(0)][1].split()))))