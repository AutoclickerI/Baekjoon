l=[31*['']for _ in[0]*31]
d=0
x=-15
y=15
while x!=0 or y!=0:
    l[x][y]='DXAW'[d]
    x+=d==0
    y-=d==1
    x-=d==2
    y+=d==3
    if l[x][y]:
        l[x-(d==0)+(d==2)][y-(d==3)+(d==1)]='DXAW'[d+1&3]
        x+=1-(d<2)*2
        y+=(0<d<3)*2-1
        d=d+1&3
for _ in[0]*int(input()):
    x,y=map(int,input().split())
    while s:=l[x][y]:
        print(end=s)
        if s=='D':x+=1
        if s=='X':y-=1
        if s=='A':x-=1
        if s=='W':y+=1
    print()