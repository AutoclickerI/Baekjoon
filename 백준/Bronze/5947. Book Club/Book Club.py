(N,_,P),*l=[[*map(int,i.split())]for i in open(0)]
print(sum(all(i[j-1]==k for j,k in l[N:])for i in l[:N]))