*l,=map(int,open(0).read().split())
print(sum(l)-min(max(l[:3]),max(l[3:]))*2)