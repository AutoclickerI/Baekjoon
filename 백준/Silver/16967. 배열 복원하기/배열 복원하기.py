[W,H,Y,X],*b=[[*map(int,i.split())]for i in open(0)]
arr=[H*[-1]for _ in[0]*W]
def getv(y,x):
    if 0<=y<W and 0<=x<H:
        return arr[y][x]
    return 0

c=W*H
while c:
    for y in range(W):
        for x in range(H):
            p=arr[y][x]
            q=getv(y-Y,x-X)
            if p==q==-1:
                pass
            elif p==-1:
                arr[y][x]=b[y][x]-q
                c-=1
            elif q==-1:
                arr[y-Y][x-X]=b[y][x]-p
                c-=1
            p=arr[y][x]
            q=getv(y+Y,x+X)
            if p==q==-1:
                continue
            if p==-1:
                arr[y][x]=b[y+Y][x+X]-q
                c-=1
            if q==-1:
                arr[y+Y][x+X]=b[y+Y][x+X]-p
                c-=1
            
for i in arr:print(*i)