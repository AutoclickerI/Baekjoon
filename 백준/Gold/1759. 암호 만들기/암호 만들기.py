from itertools import*
L,C,*l=open(0).read().split()
for w in combinations(sorted(l),L:=int(L)):0<sum(map(w.count,'aeiou'))<L-1and print(*w,sep='')