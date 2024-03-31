N,D=map(int, input().split())
P=N//2
print(*{*range(D-P,D+P+1)}-{N%2*1e9+D})