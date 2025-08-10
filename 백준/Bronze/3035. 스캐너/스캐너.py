_,_,a,b,*s=open(0).read().split()
for c in s:print(*[''.join(d*int(b)for d in c)]*int(a))