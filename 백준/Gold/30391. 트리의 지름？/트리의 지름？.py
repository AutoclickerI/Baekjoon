N,K=map(int,input().split())
c=K-2
for i in range(1,N):
    print(max(1,c//(K-1)),i+1)
    c+=1