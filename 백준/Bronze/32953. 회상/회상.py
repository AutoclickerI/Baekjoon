l=open(0).read().split()
print(sum(int(l[1])<=len(i)//8*l.count(i)for i in{*l}))