n,s=open(0)
n=int(n)
[print(end=s[j*n+[i,n+~i][j%2]])for i in range(n)for j in range(len(s)//n)]