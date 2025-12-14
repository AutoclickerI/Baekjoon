[N,M]=map(int,input().split())
d={}
for _ in[0]*N:
    s=input()
    d[s]=d.get(s,0)+1
r=0
K=int(input())
for i in d:
    v=K-i.count('0')
    if 0<=v and v%2<1:
        r=max(r,d[i])
print(r)