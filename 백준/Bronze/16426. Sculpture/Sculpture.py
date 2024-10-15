(n,m),*l=[[*map(int,i.split())]for i in open(0)]
for i in range(n):print(*(+(n-1>i>0<j<m-1and l[i][j]<min(l[i+1][j],l[i-1][j],*l[i][j-1:j+2:2]))for j in range(m)))