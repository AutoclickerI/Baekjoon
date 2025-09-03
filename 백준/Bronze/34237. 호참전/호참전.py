(N,M),*l=[[*map(int,i.split())]for i in open(0)]
for g,x,y in l[N:]:print(sum(y<=j<=g-i<=g-x for i,j in l[:N]))