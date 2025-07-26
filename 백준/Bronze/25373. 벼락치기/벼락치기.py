n=int(input())
print(min((n+k*-~k//2-1)//k for k in range(1,8)))