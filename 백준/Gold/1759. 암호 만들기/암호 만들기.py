L,C,*l=open(0).read().split()
for w in __import__('itertools').combinations(sorted(l),L:=int(L)):0<sum(map(w.count,'aeiou'))<L-1and print(*w,sep='')