(K,N),*l=[[*map(int,i.split())]for i in open(0)]
R=range(N)
print(sum(sum(j+1in v[:v.index(i+1)]for v in l)%K<(i<j)for i in R for j in R))