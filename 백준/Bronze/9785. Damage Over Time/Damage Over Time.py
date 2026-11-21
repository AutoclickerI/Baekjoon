(N,M),*l=[[*map(int,i.split())]for i in open(0)]
p,q=zip(*sorted(l)[:~M:-1])
print(sum(p),min(q))