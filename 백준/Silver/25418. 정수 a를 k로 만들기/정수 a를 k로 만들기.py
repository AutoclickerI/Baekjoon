A,K=map(int,input().split())
c=0
while 2*A<=K:c+=1+K%2;K//=2
print(c+K-A)