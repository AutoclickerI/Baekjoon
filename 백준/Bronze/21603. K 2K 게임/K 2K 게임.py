N,K=map(int,input().split())
l=[i for i in range(1,N+1)if K%10!=i%10!=2*K%10]
print(len(l))
print(*l)