N,*l=map(int,open(0).read().split())
s=sum(l)
print(sum(i*(s-i)for i in l)//2)