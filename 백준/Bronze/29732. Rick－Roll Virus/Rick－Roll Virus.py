i,s=open(0)
N,M,K=map(int,i.split())
print('YNeos'[M<sum('R'in s[max(i-K,0):i-~K]for i in range(N))::2])