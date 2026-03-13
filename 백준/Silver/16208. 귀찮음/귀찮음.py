N,*l=map(int,open(0).read().split())
l.sort()
v=sum(l)
r=0
for i in l:
    v-=i
    r+=i*v
print(r)