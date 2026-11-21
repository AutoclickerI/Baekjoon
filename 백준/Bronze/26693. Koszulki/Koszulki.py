n,k,*l=map(int,open(0).read().split())
l.sort()
print(max(i*(l[~i]==l[-k])for i in range(n))+1)