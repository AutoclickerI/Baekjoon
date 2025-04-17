def move(n,cube):
    b=[*cube]
    if n==0:
        n1 = b[1]; n2 = b[3]; n3 = b[12];
        b[1] = b[22];
        b[3] = b[20];
        b[20] = b[19];
        b[22] = b[17];
        b[17] = b[5];
        b[19] = b[7];
        b[5] = n1;
        b[7] = n2;

        b[12] = b[13];
        b[13] = b[15];
        b[15] = b[14];
        b[14] = n3;

    elif n==1:
        n1 = b[4]; n2 = b[5]; n3 = b[0];
        b[4] = b[8];
        b[5] = b[9];
        b[8] = b[20];
        b[9] = b[21];
        b[20] = b[12];
        b[21] = b[13];
        b[12] = n1;
        b[13] = n2;

        b[0] = b[1];
        b[1] = b[3];
        b[3] = b[2];
        b[2] = n3;

    else:
        n2 = b[2]; n1 = b[3]; n3 = b[4];
        b[2] = b[12];
        b[3] = b[14];
        b[14] = b[16];
        b[12] = b[17];
        b[16] = b[9];
        b[17] = b[11];
        b[9] = n1;
        b[11] = n2;

        b[4] = b[5];
        b[5] = b[7];
        b[7] = b[6];
        b[6] = n3;
        
    return ''.join(b)

from collections import deque

while 1:
    b=[input()for _ in[0]*6]
    if b[0][2]=='.':
        break
    cube=''
    for y,x in(0,2),(2,2),(2,0),(2,4),(4,2),(2,6):
        cube+=b[y][x:x+2]+b[y+1][x:x+2]
    
    cube_end=[*cube]
    cube_end[16]=cube_end[17]=cube_end[19]=cube_end[18]
    cube_end[20]=cube_end[21]=cube_end[22]=cube_end[23]
    cube_end[8]=cube_end[9]=cube_end[11]=cube_end[10]
    
    corners=((2,9,4),(3,5,12),(1,13,20),(0,8,21),(6,11,16),(7,17,14),(19,15,22))
    per=((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,1,0),(2,0,1))
    
    for i in range(7):
        for j in range(6):
            p=cube[corners[i][per[j][0]]]
            q=cube[corners[i][per[j][1]]]
            r=cube[corners[i][per[j][2]]]
            if p==cube[18]and q==cube[23]:
                cube_end[12]=cube_end[13]=cube_end[14]=cube_end[15]=r
            if p==cube[10]and q==cube[23]:
                cube_end[0]=cube_end[1]=cube_end[2]=cube_end[3]=r
            if p==cube[10]and q==cube[18]:
                cube_end[4]=cube_end[5]=cube_end[6]=cube_end[7]=r
    
    cube_end=''.join(cube_end)
    
    sol_start={}
    sol_end={}
    
    cub_start=deque()
    cub_end=deque()
    
    sol_start[cube]=''
    cub_start+=cube,
    sol_end[cube_end]=''
    cub_end+=cube_end,
    
    conti=1
    
    while conti:
        b=cub_start.popleft()
        for i in range(6):
            t=b
            for _ in[0]*(1+i//3*2):
                t=move(i%3,t)
            if t not in sol_start:
                sol_start[t]=sol_start[b]+'XYZ'[i%3]*(1+i//3*2)
                cub_start+=t,
        
        e=cub_end.popleft()
        for i in range(6):
            t=e
            for _ in[0]*(1+i//3*2):
                t=move(i%3,t)
            if t in sol_start:
                print(sol_start[t]+'XYZ'[i%3]*(3-i//3*2)+sol_end[e][::-1])
                conti=0
                break
            if t not in sol_end:
                sol_end[t]=sol_end[e]+'XYZ'[i%3]*(3-i//3*2)
                cub_end+=t,
    
    input()