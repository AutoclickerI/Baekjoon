N,M,K=map(int,input().split())
s=input()
print('YNeos'[M<sum('R'in s[max(i-K,0):i-~K]for i in range(N))::2])