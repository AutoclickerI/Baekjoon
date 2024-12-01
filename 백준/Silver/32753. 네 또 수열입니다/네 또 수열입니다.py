N,K=map(int,input().split())
if (N,K)==(2,1):
    print(1,2)
elif N<2:
    print(*'1'*K)
else:
    print(-1)