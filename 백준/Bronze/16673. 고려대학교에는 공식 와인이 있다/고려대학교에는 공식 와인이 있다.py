C,K,P=map(int,input().split())
print(sum(K*i+P*i*i for i in range(1,1+C)))