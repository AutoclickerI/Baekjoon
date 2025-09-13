n,k=map(int,input().split())
m=n//k
q=k//m
print(m*q*(k%m+m*~-q//2))