n=int(input())
s={input()for _ in[0]*n}

input()
T=int(input())

def backtrack(ss,y,x):
    re.add(ss)
    if len(ss)==8:
        return
    for dy in-1,0,1:
        for dx in-1,0,1:
            if dy==dx==0:continue
            ny,nx=y+dy,x+dx
            if 0<=ny<4 and 0<=nx<4 and v[ny][nx]<1:
                v[ny][nx]=1
                backtrack(ss+b[ny][nx],ny,nx)
                v[ny][nx]=0
for i in range(T):
    b=[input()for _ in[0]*4]
    if i<T-1:
        input()
    re=set()
    v=[4*[0]for _ in[0]*4]
    for y in range(4):
        for x in range(4):
            v[y][x]=1
            backtrack(b[y][x],y,x)
            v[y][x]=0
    jl=re&s
    m=min(jl,key=lambda s:(-len(s),s))
    print(sum([0,0,0,1,1,2,3,5,11][len(i)]for i in jl),m,len(jl))