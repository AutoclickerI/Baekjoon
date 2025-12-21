import sys
input=sys.stdin.readline

N,K=map(int,input().split())
K+=1
v=[0]*22
l=[len(input())for _ in[0]*N]
r=0
for i in l[:K]:r+=v[i];v[i]+=1
for i in range(N-K):
    v[l[i]]-=1
    r+=v[l[i+K]]
    v[l[i+K]]+=1
print(r)