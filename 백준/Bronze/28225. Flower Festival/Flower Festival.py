k=0
(n,s),*a=[map(int,s.split())for s in open(0)]
print(min(((s-i)/j,k:=k+1)for i,j in a)[1])