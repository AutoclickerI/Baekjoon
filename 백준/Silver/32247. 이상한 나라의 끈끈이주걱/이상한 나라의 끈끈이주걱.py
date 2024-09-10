N,M=map(int,input().split())
posx=posy=0
flag=0

db=sorted([[*map(int,input().split())]for _ in[0]*M],key=lambda s:s[1])

for c,x,y in db:
    
    dx=x-posx
    posy-=dx
    if c<1:
        posy=max(posy,y+1)
    elif y<=posy:
        flag=1
    posx=x
if flag or posy-(N-posx)>0:
    print('adios')
else:
    print('stay')