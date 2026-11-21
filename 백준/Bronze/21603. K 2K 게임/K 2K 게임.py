N,K=map(int,input().split())
print(len(l:=[i for i in range(1,N+1)if K%10!=i%10!=2*K%10]),*l)