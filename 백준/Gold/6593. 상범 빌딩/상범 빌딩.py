while'1'<(s:=input()):
    L,R,C=map(int,s.split())
    b=[[input()for _ in[0]*-~R]for _ in[0]*L]
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if b[z][y][x]=='S':
                    s=z,y,x
                if b[z][y][x]=='E':
                    e=z,y,x
    v=[[C*[0]for _ in[0]*R]for _ in[0]*L]
    l=[(0,*s)]
    for c,z,y,x in l:
        if(z,y,x)==e:
            break
        for dz,dy,dx in(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1):
            nz,ny,nx=z+dz,y+dy,x+dx
            if 0<=nz<L and 0<=ny<R and 0<=nx<C and b[nz][ny][nx]!='#'and v[nz][ny][nx]<1:
                v[nz][ny][nx]=1
                l+=(c+1,nz,ny,nx),
    else:
        print('Trapped!')
        continue
    print('Escaped in',c,'minute(s).')