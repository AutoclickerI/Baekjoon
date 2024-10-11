M,N=map(int,input().split())
print(len({i/j for i in range(M,N+1)for j in range(M,N+1)}))