n,*l=map(int,open(0).read().split())
a=l[0]
l[0]=min(l[:2])
for i in range(1,n):
 if a<l[i]:a,l[i]=l[i],a
 else:l[i]=max(l[i],l[i-1])
print(*l[1:])