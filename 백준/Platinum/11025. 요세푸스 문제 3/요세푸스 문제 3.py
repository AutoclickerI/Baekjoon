N,K=map(int,input().split())
x=n=0
while n<N:n+=1;x=(x+K)%n
print(x+1)