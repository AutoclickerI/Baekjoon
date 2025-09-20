N,M=map(int,input().split())
b=[input()[::2]for _ in[0]*N]

cc=[]

for y in range(N):
    for x in range(M):
        if b[y][x]not in'06':cc+=(y,x),

def traverse(y,x,dy,dx):
    if 0<=y<N and 0<=x<M and tes[y][x]!='6':
        if tes[y][x]=='0':tes[y][x]='#'
        traverse(y+dy,x+dx,dy,dx)

def evaluate():
    for i in range(len(cc)):
        y,x=cc[i]
        c_t=b[y][x]
        if c_t=='1':d=0,
        if c_t=='2':d=0,2
        if c_t=='3':d=0,1
        if c_t=='4':d=0,1,2
        if c_t=='5':d=0,1,2,3
        for c in d:
            dy,dx=[(-1,0),(0,1),(1,0),(0,-1)][c+rot[i]&3]
            traverse(y,x,dy,dx)
    return sum(j=='0'for i in tes for j in i)
        
m=1e9
for i in range(4**len(cc)):
    tes=[[*i]for i in b]
    rot=[]
    for _ in[0]*len(cc):rot+=i%4,;i//=4
    m=min(m,evaluate())

print(m)