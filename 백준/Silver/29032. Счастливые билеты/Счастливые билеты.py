N,M=map(int,input().split())
print(sum(M>=N-10**(i//9+1)//9*(i%9+1)>-1for i in range(81)))