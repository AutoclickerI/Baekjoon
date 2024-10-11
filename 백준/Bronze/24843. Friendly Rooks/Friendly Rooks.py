n,m,k=map(int,input().split())
if k>min(n,m):print('Impossible')
else:print('Possible',*['.'*m]*(n-k),*['.'*i+'*'+'.'*(m+~i)for i in range(k)],sep='\n')