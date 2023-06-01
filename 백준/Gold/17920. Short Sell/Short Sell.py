N,K=map(int,input().split())
a=N=0
for i in map(int,input().split()):N=max(max(N,p:=100*i)-K,0);a=max(a,N-p)
print(a)