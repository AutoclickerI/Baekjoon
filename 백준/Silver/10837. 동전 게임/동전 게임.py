import sys
input=sys.stdin.readline

def check(N,M,K):
    if N<1:
        if K-M+1<M-1:
            return 0
        else:
            return 1
    if M<1:
        if K-N+1<N:
            return 0
        else:
            return 1
K=int(input())
for _ in[0]*int(input()):
    M,N=map(int,input().split())
    v=min(M,N)
    print(check(N-v,M-v,K-v))