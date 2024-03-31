N,D=map(int,input().split())
print(*{*range(D-N//2,D+N//2+1)}-{N%2*1e9+D})