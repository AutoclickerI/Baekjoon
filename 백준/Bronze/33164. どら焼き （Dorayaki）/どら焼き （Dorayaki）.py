_,A,B=[[*map(int,i.split())]for i in open(0)]
print(sum(max(a,b)*(a+b)for a in A for b in B))