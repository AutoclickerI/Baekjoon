N,M=map(int,input().split())
i=0
while N*M%2:i+=1;N//=2;M//=2
print(-1-4**i//-3)