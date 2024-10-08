n,*l=map(int,open(0).read().split())
print(*sorted(i for i in range(51)if l.count(i)>n*2)or[-1])