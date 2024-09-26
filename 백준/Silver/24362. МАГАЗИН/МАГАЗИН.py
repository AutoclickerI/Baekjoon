n,k,*l=map(int,open(0).read().split())
l.sort()
print(sum(l[-i]for i in range(1,n+1)if i%k))