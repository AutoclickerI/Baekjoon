N,M,A=map(int,input().split())
m=M//2+1
while s:=int(input())-m:print(A:=1+(A+s-1)%N)
print(0)