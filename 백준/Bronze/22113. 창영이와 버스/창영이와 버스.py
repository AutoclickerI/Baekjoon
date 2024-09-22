_,b,*c=[[*map(int,i.split())]for i in open(0)]
print(sum(c[i-1][j-1]for i,j in zip(b,b[1:])))