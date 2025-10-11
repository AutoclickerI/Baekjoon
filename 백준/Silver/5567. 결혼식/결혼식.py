N=int(input())
M=int(input())

edges=[[]for _ in[0]*N]

for _ in[0]*M:
    a,b=map(int,input().split())
    edges[a-1]+=b-1,
    edges[b-1]+=a-1,

s={*edges[0]}
for i in edges[0]:
    s|={*edges[i]}
print(len(s-{0}))