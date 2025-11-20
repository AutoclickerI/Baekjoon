N,K=map(int,input().split())
N+=1
v=[N*[0]for _ in[0]*N]

for _ in[0]*K:
    s,e=map(int,input().split())
    v[s][e]=-1
    v[e][s]=1

for m in range(N):
    for s in range(N):
        for e in range(N):
            if v[s][e]==0 and v[s][m]==v[m][e]:
                v[s][e]=v[s][m]

for _ in[0]*int(input()):
    s,e=map(int,input().split())
    print(v[s][e])