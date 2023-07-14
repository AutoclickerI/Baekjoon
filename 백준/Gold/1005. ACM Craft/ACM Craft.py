import sys
sys.setrecursionlimit(2*10**5)
def recur(n):
    if n not in cache:cache[n]=max([0,*map(recur,build[n])])+l[n]
    return cache[n]
for _ in[0]*int(input()):
    N,K=map(int,input().split())
    l=[0,*map(int,input().split())]
    build=[[]for _ in[0]*(N+1)]
    for _ in[0]*K:
        p,q=map(int,input().split())
        build[q]+=[p]
    cache={}
    print(recur(int(input())))