n,*l=map(int,open(0).read().split())
a=[0,0]
for i in l:a+=i-sum(a[-2:]),
print(*a)