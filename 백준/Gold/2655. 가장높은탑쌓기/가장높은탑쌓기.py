[N],*l=[[*map(int,i.split())]for i in open(0)]
N+=1
l=[0,0,0],*l
w=[N*[-float('inf')]for _ in[0]*N]
mc=[[[]for _ in[0]*N]for _ in[0]*N]
for s in range(N):
    for e in range(N):
        if l[s][0]<l[e][0]and l[s][2]<l[e][2]:
            w[s][e]=l[e][1]
            mc[s][e]+=s,e

for m in range(N):
    for s in range(N):
        for e in range(N):
            if w[s][e]<w[s][m]+w[m][e]:
                w[s][e]=w[s][m]+w[m][e]
                mc[s][e]=mc[s][m][:-1]+mc[m][e]

y,x=max([(y,x)for y in range(N)for x in range(N)],key=lambda i:w[i[0]][i[1]])

v=mc[y][x][1:]
print(len(v),*v)