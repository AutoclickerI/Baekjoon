A,B=map(int,input().split())
m=10**9+7
print((1//A*B or~-pow(A,B,m)*pow(A-1,-1,m))%m)