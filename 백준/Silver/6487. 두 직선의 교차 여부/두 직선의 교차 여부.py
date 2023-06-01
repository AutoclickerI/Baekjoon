import math
for _ in[0]*int(input()):
    x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
    g1=[y2-y1,x2-x1]
    if g1[1]==0:g1[0]=1
    else:
        m=math.gcd(*g1)
        g1[1]//=m
        g1[0]//=m
        if g1[1]<0:g1[0]*=-1;g1[1]*=-1
    g2=[y4-y3,x4-x3]
    if g2[1]==0:g2[0]=1
    else:
        m=math.gcd(*g2)
        g2[1]//=m
        g2[0]//=m
        if g2[1]<0:g2[0]*=-1;g2[1]*=-1
    g3=[y2-y3,x2-x3]
    if g3[1]==0:g3[0]=1
    else:
        m=math.gcd(*g3)
        g3[1]//=m
        g3[0]//=m
        if g3[1]<0:g3[0]*=-1;g3[1]*=-1
    if g1==g2:
        if g1==g3:
            print('LINE')
        else:
            print('NONE')
    else:
        if g1[1]==0:
            print(f'POINT {x1:.2f} {g2[0]/g2[1]*(x1-x3)+y3:.2f}')
        else:
            x=(y1-y3+g2[0]/g2[1]*x3-g1[0]/g1[1]*x1)/(g2[0]/g2[1]-g1[0]/g1[1])
            print(f'POINT {x:.2f} {g2[0]/g2[1]*(x-x3)+y3:.2f}')