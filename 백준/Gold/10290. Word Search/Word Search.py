def find(y,x,dy,dx,m=0,n=0):
    if n==len(s):
        return 1
    if H>x>=0<=y<W and l[y][x]==s[n]:
        v[y][x]=max(m,v[y][x])
        return find(y+dy,x+dx,dy,dx,m,n+1)
    return 0
for T in[0]*int(input()):
    N,W,H=map(int,input().split())
    l=eval('[*input()],'*W)
    v=eval('[0]*H,'*W)
    possible=1
    for _ in[0]*N:
        s=input()
        d=[]
        for y in range(W):
            for x in range(H):
                if len(s)==1 and find(y,x,0,0):
                    d+=(y,x,0,0),
                    continue
                for dy in range(-1,2):
                    for dx in range(-1,2):
                        if dy==dx==0:
                            continue
                        if find(y,x,dy,dx):
                            d+=(y,x,dy,dx),

        if d:
            if len(d)==1:
                [y,x,dy,dx],=d
                find(y,x,dy,dx,2)
            else:
                z=1
                if len(d)==2:
                    [y1,x1,dy1,dx1],[y2,x2,dy2,dx2]=d
                    if s==s[::-1] and(y1+(len(s)-1)*dy1,x1+(len(s)-1)*dx1)==(y2,x2):
                        z+=1
                for y,x,dy,dx in d:
                    find(y,x,dy,dx,z)
        else:
            possible=0
    if possible:
        ambiguous=0
        for y in range(W):
            for x in range(H):
                if v[y][x]:
                    l[y][x]=''
                    ambiguous|=v[y][x]<2
        if ambiguous:
            print('ambiguous')
        else:
            print(''.join(map(''.join,l))or'empty solution')
    else:
        print('no solution')