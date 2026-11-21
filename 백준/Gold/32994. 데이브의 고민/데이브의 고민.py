N,M=map(int,input().split())
s='12345'*201
for i in range(N):
    print(*s[i*2%5:i*2%5+M])