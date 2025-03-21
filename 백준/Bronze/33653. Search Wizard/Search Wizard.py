S=input();
M=len(S)
input()
T=input();
N=len(T)
print(sum(S==T[i:i+M]for i in range(N)))