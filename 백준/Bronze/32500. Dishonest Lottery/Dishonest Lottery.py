n,*a=map(int,open(0).read().split())
print(*[i for i in range(51)if a.count(i)>n*2]or[-1])