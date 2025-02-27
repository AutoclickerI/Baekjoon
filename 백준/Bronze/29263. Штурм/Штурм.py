(n,m),*l=[[*map(int,i.split())]for i in open(0)]
print(n*m-sum(any(n>I>-1<J<m>0<l[i][j]<=l[I][J]for I,J in((i-1,j),(i+1,j),(i,j-1),(i,j+1)))for i in range(n)for j in range(m)))