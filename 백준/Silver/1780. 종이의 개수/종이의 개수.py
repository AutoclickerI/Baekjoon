n=int(input())
l=[[*map(int,input().split())]for _ in[0]*n]
v=[0]*3
def rec(x,y,c):
    z=l[x][y]
    f=0
    for i in range(x,x+c):
        for j in range(y,y+c):
            f+=l[i][j]!=z
    if f:
        for i in[0,c//3,c//3*2]:
            for j in[0,c//3,c//3*2]:
                rec(x+i,y+j,c//3)
    else:
        v[z]+=1
rec(0,0,n)
print(v[2],v[0],v[1])