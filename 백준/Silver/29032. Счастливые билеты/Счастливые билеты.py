N,M=map(int,input().split())
print(sum(M>=N-int(str(i%9+1)*(i//9+1))>-1for i in range(81)))