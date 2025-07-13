_,M,*l=open(0).read().split()
print(sum(int(M)<=len(i)//8*l.count(i)for i in{*l}))