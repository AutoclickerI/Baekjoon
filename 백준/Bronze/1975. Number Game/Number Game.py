f=lambda n,b:n%b<1and-~f(n//b,b)
for i in[*open(0)][1:]:n=int(i);print(sum(f(n,b+2)for b in range(n)))