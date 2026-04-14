M,M,*l=map(int,open(0).read().split())
h=[0]*M
l.sort()
while l:h[h.index(min(h))]+=l.pop()
print(max(h))