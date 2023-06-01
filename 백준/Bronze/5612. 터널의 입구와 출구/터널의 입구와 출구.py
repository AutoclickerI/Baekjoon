n=int(input())
l=[m:=int(input())]
for i in[0]*n:p,q=map(int,input().split());l+=[m:=m+p-q]
print(max(l)if min(l)>=0 else 0)