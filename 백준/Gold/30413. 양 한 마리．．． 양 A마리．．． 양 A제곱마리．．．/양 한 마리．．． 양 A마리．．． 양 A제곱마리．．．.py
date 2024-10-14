A,B=map(int,input().split())
print((~-pow(A,B,M:=10**9+7)*pow(A-1,M-2,M)or B)%M)