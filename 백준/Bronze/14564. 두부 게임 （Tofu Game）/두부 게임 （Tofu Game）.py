N,M,A=map(int,input().split())
m=M//2+1
while s:=int(input())-m:A=1+(A+s-1)%N;print(A)
print(0)