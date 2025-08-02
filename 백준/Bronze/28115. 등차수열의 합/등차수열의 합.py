n,*a=map(int,open(0).read().split())
V=1<len({*map(int.__sub__,a,a[1:])})
print('YNEOS'[V::2])
V or print(*a+[0]*n)