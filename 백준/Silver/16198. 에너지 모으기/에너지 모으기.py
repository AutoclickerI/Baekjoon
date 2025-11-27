N,*W=map(int,open(0).read().split())
f=lambda W:max([W[i-2]*W[i]+f(W[:i-1]+W[i:])for i in range(2,len(W))]+[0])
print(f(W))