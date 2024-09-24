N,M=map(int,input().split())
print(sum(M>=N-int(str(j+1)*-~i)>-1for i in range(9)for j in range(9)))