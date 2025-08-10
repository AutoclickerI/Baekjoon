n,k,*l=map(int,open(0).read().split())
print(max(sum(l[i:i+k])for i in range(n-k+1)))