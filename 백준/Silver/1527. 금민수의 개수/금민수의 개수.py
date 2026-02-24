s=lambda n:n<=e and(b<=n)+s(n*10+4)+s(n*10+7)
b,e=map(int,input().split())
print(s(0))