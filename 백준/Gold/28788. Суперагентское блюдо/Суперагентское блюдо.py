import sys
input=sys.stdin.readline

N=int(input())

l=input().split()

c={}
for _ in[0]*int(input()):
    p,q=input().split()
    c[p]=int(q)

d={}

for _ in[0]*int(input()):
    _,s,*z=input().split()
    d[s]=z

dp={}

def DFS(s):
    if s not in dp:
        v=0
        for i in d.get(s,[]):
            v+=DFS(i)
        if v<1:v=float('inf')
        dp[s]=min(v,c.get(s,float('inf')))
    return dp[s]

s=0
for i in l:s+=DFS(i)

if s==float('inf'):
    print(-1)
else:
    print(s)