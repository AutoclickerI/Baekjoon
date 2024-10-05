n,k,*l=map(int,open(0).read().split())
l=sorted(l)[::-1]
print(max(i*(l[i]==l[k-1])for i in range(n))+1)