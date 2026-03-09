N,K,*l=map(int,open(0).read().split())
l.sort()
p=l[0]
l+=float('inf'),
c=1
for i in l[1:]:
    if (i-p)*c<=K:
        K-=(i-p)*c
        c+=1
        p=i
print(p+K//c)