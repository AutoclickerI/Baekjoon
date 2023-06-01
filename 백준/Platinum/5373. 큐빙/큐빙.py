def cw(l):
    return[l[6],l[3],l[0],l[7],l[4],l[1],l[8],l[5],l[2]]
def ccw(l):
    return cw(cw(cw(l)))
for _ in[0]*int(input()):
    cube=[[i]*9 for i in'wrgbyo']
    input()
    for i in input().split():
        n=i[0]
        d=i[1]
        if n=='U':
            if d=='+':
                cube[0]=cw(cube[0])
                cube[1][:3],cube[2][:3],cube[5][:3],cube[3][:3]=cube[3][:3],cube[1][:3],cube[2][:3],cube[5][:3]
            else:
                cube[0]=ccw(cube[0])
                cube[1][:3],cube[2][:3],cube[5][:3],cube[3][:3]=cube[2][:3],cube[5][:3],cube[3][:3],cube[1][:3]
        elif n=='D':
            if d=='+':
                cube[4]=cw(cube[4])
                cube[1][6:],cube[2][6:],cube[5][6:],cube[3][6:]=cube[2][6:],cube[5][6:],cube[3][6:],cube[1][6:]
            else:
                cube[4]=ccw(cube[4])
                cube[1][6:],cube[2][6:],cube[5][6:],cube[3][6:]=cube[3][6:],cube[1][6:],cube[2][6:],cube[5][6:]
        elif n=='F':
            if d=='-':
                cube[1]=ccw(cube[1])
                cube[0][6:],cube[3][6::-3],cube[4][:3],cube[2][8::-3]=cube[3][::3],cube[4][:3],cube[2][2::3],cube[0][6:]
            else:
                cube[1]=cw(cube[1])
                cube[0][6:],cube[3][::3],cube[4][:3],cube[2][2::3]=cube[2][8::-3],cube[0][6:],cube[3][6::-3],cube[4][:3]
        elif n=='B':
            if d=='-':
                cube[5]=ccw(cube[5])
                cube[0][:3],cube[3][2::3],cube[4][6:],cube[2][::3]=cube[2][6::-3],cube[0][:3],cube[3][8::-3],cube[4][6:]
            else:
                cube[5]=cw(cube[5])
                cube[0][:3],cube[3][8::-3],cube[4][6:],cube[2][6::-3]=cube[3][2::3],cube[4][6:],cube[2][::3],cube[0][:3]
        elif n=='L':
            if d=='-':
                cube[2]=ccw(cube[2])
                cube[0][::3],cube[1][::3],cube[4][::3],cube[5][8::-3]=cube[1][::3],cube[4][::3],cube[5][8::-3],cube[0][::3]
            else:
               cube[2]=cw(cube[2])
               cube[0][::3],cube[1][::3],cube[4][::3],cube[5][8::-3]=cube[5][8::-3],cube[0][::3],cube[1][::3],cube[4][::3]
        else:
            if d=='-':
                cube[3]=ccw(cube[3])
                cube[0][2::3],cube[1][2::3],cube[4][2::3],cube[5][6::-3]=cube[5][6::-3],cube[0][2::3],cube[1][2::3],cube[4][2::3]
            else:
                cube[3]=cw(cube[3])
                cube[0][2::3],cube[1][2::3],cube[4][2::3],cube[5][6::-3]=cube[1][2::3],cube[4][2::3],cube[5][6::-3],cube[0][2::3]
    print(*cube[0][:3],'\n',*cube[0][3:6],'\n',*cube[0][6:],sep='')