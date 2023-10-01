n,*l=map(int,open(0).read().split())
if sum(l)%2:
    print((sum(l)-min(i for i in l if i%2))//2)
else:
    print(sum(l)//2)