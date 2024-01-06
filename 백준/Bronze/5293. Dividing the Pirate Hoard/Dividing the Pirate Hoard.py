M,P=map(int,input().split())
print(*eval("M-(M:=M//P*~-P),"*P))
print(M)