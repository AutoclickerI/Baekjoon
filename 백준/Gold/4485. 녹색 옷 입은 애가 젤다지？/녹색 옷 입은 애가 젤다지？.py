from heapq import*
i=0
while n:=int(input()):
    i+=1
    b=eval('[*map(int,input().split())],'*n)
    v=eval('[1]*n,'*n)
    c=eval('[1e9]*n,'*n)
    c[0][0]=b[0][0]
    hq=[[b[0][0],0,0]]
    while v[-1][-1]:
        p,y,x=heappop(hq)
        if c[y][x]<p:
            continue
        v[y][x]=0
        for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
            if 0<=y+dy<n>x+dx>=0 and p+b[y+dy][x+dx]<c[y+dy][x+dx]:
                c[y+dy][x+dx]=p+b[y+dy][x+dx]
                heappush(hq,[p+b[y+dy][x+dx],y+dy,x+dx])
    print(f'Problem {i}:',c[-1][-1])