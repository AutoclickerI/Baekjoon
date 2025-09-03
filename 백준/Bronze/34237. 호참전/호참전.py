(N,M),*l=[[*map(int,i.split())]for i in open(0)]
for g,x,y in l[N:]:print(sum(x<=i and y<=j and i+j<=g for i,j in l[:N]))