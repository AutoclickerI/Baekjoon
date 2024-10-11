n,m,k=map(int,input().split())
print(*['Impossible']*(k>min(n,m))or['Possible']+['.'*m]*(n-k)+['.'*i+'*'+'.'*(m+~i)for i in range(k)],sep='\n')