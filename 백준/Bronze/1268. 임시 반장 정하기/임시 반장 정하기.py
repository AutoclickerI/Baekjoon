l=[[*map(int,i.split())]for i in[*open(0)][1:]]
print(min(enumerate(l),key=lambda s:(sum(all(j!=k for j,k in zip(i,s[1]))for i in l),s[0]))[0]+1)