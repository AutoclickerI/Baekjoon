import sys
input=sys.stdin.readline

for T in range(1,int(input())+1):
    N,K=map(int,input().split())
    s=input()
    v=sum(s[i]!=s[N-1-i]for i in range(N//2))
    print(f'Case #{T}:',abs(K-v))