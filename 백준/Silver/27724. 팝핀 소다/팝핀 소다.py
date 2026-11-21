N,M,K=map(int,input().split())
K-=1
a=0
while K:
    K-=1
    K//=2
    a+=1
t=0
while N:=N//2:t+=1
print(min(a+M,t))