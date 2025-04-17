import sys
input=sys.stdin.readline

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

def decode(b):
    cube=''
    for y,x in(0,2),(2,2),(2,0),(2,4),(4,2),(2,6):
        cube+=b[y][x:x+2]+b[y+1][x:x+2]
    return cube

from collections import deque

cube_orig=''.join(4*str(i)for i in range(6))
hmap={cube_orig:0}

dq=deque([(cube_orig,0)])
while dq:
    b,c=dq.popleft()
    for i in range(6):
        t=b
        for _ in[0]*(1+i//3*2):
            t=move(i%3,t)
        if t not in hmap:
            hmap[t]=c+1
            dq+=(t,c+1),

def roll_x(s):
    return''.join(s[i]for i in[2,0,3,1,12,13,14,15,4,5,6,7,20,21,22,23,17,19,16,18,8,9,10,11])

def roll_y(s):
    return''.join(s[i]for i in[4,5,6,7,16,17,18,19,9,11,8,10,14,12,15,13,23,22,21,20,3,2,1,0])

def checksum(s):
    return s[10]+s[18]+s[23]

T=int(input())

while T:
    T-=1
    input()
    b=[input()for _ in[0]*6]
    
    mp={}
    
    cube=decode([i[:8]for i in b])
    
    for x in(0,8,21),(1,13,20),(2,4,9),(3,5,12),(6,11,16),(7,14,17),(15,19,22),(10,18,23):
        p,q=zip(*sorted((cube[i],i)for i in x))
        mp[p]=q
    
    mp2={}
    
    cube_end=decode([i[9:]for i in b])
    
    z=['.']*24
    for x in(0,8,21),(1,13,20),(2,4,9),(3,5,12),(6,11,16),(7,14,17),(15,19,22),(10,18,23):
        p,q=zip(*sorted((cube_end[i],i)for i in x))
        mp2[p]=q
        for i,j in zip(q,mp[p]):
            z[i]=str(j//4)
    
    cube_end=''.join(z)
    se=set()
    
    for _ in range(4):
        for i in range(4):
            se.add(cube_end)
            cube_end=roll_x(cube_end)
        cube_end=roll_y(cube_end)
    
    cube_end=roll_x(cube_end)
    cube_end=roll_y(cube_end)
    for i in range(4):
        se.add(cube_end)
        cube_end=roll_x(cube_end)
        
    cube_end=roll_y(cube_end)
    cube_end=roll_y(cube_end)
    for i in range(4):
        se.add(cube_end)
        cube_end=roll_x(cube_end)
    
    for i in se:
        if checksum(i)=='245':
            cube_end=i
            break
    else:
        raise
    
    print(hmap[cube_end])