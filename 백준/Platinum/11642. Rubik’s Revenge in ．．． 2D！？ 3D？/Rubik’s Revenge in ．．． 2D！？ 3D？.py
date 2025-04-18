def rotate(b,c,i,z):
    b=[*b]
    if c==0:
        *s,=range(4*i,4*i+4)
        e=*s[1+z*2:],*s[:1+z*2]
    if c==1:
        *s,=range(i,16,4)
        e=*s[1+z*2:],*s[:1+z*2]
    t=[b[i]for i in s]
    for i,c in zip(e,t):b[i]=c
    return''.join(b)

cube=''.join(input()for _ in[0]*4)
cube_end='RRRRGGGGBBBBYYYY'

start_map={cube:0}
end_map={cube_end:0}

from collections import deque

dq_start=deque([cube])
dq_end=deque([cube_end])

if cube==cube_end:
    print(0)
else:
    mv=14
    
    while dq_start or dq_end:
        if dq_start:
            s=dq_start.popleft()
            c=start_map[s]
            if mv<=c*2:
                dq_start=[]
                continue
            else:
                for i in range(16):
                    t=rotate(s,i//8,i%8//2,i%2)
                    if t not in start_map:
                        if t in end_map:
                            mv=min(mv,c+1+end_map[t])
                        start_map[t]=c+1
                        dq_start+=t,
        if dq_end:
            e=dq_end.popleft()
            c=end_map[e]
            if mv<=c*2:
                dq_end=[]
                continue
            else:
                for i in range(16):
                    t=rotate(e,i//8,i%8//2,i%2)
                    if t not in end_map:
                        if t in start_map:
                            mv=min(mv,c+1+start_map[t])
                        end_map[t]=c+1
                        dq_end+=t,
        
    print(mv)