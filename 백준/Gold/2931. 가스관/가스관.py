R,C=map(int,input().split())
b=[input()for _ in[0]*R]

def check(y,x,dy,dx):
    if b[y][x]!='.':
        return 0
    ny,nx=y+dy,x+dx
    if 0<=ny<R and 0<=nx<C:
        if b[ny][nx]in'MZ':
            return 0.5
        if b[ny][nx]=='+':
            return 1
        if b[ny][nx]=='-':
            return(dy,dx)in[(0,-1),(0,1)]
        if b[ny][nx]=='|':
            return(dy,dx)in[(1,0),(-1,0)]
        if b[ny][nx]=='1':
            return(dy,dx)in[(0,-1),(-1,0)]
        if b[ny][nx]=='2':
            return(dy,dx)in[(0,-1),(1,0)]
        if b[ny][nx]=='3':
            return(dy,dx)in[(0,1),(1,0)]
        if b[ny][nx]=='4':
            return(dy,dx)in[(0,1),(-1,0)]
    return 0

m=0
for y in range(R):
    for x in range(C):
        r=0
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            r+=check(y,x,dy,dx)
        if m<r:
            m=r
            a=y,x

y,x=a
l=[]
for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
    if check(y,x,dy,dx):
        l+=(dy,dx),
print(y+1,x+1)
if m==3:
    l=[]
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        if check(y,x,dy,dx)==1:
            l+=(dy,dx),
if len(l)==4:
    print('+')
elif l==[(-1,0),(1,0)]:
    print('|')
elif l==[(0,1),(0,-1)]:
    print('-')
elif l==[(-1,0),(0,1)]:
    print(2)
elif l==[(-1,0),(0,-1)]:
    print(3)
elif l==[(1,0),(0,1)]:
    print(1)
else:
    print(4)