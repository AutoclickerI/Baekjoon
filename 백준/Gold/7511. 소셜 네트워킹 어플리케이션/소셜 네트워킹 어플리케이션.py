import sys
input=sys.stdin.readline
sys.setrecursionlimit(2*10**5)

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

for T in range(int(input())):
    n=int(input())
    *p,=range(n+1)
    for _ in[0]*int(input()):
        s,e=sorted(map(find,map(int,input().split())))
        p[e]=s
    print(f'Scenario {T+1}:')
    for _ in[0]*int(input()):
        u,v=map(int,input().split())
        print(+(find(u)==find(v)))
    print()