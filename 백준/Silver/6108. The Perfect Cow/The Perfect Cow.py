N=int(input())
print(sorted(sorted(map(int,input().split()))[N//2]for _ in[0]*N)[N//2])