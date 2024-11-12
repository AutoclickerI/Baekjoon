import sys
input=sys.stdin.readline

q,c=map(int,input().split())
color_dict={}

def propagate(pos,color,d):
    color=-1 if color<0 else (color+1-d*2)%c
    return pos*2+d,color

for time in range(q):
    i,*j=map(int,input().split())
    s=input()[:-1]
    if i==1:
        color_dict[int('1'+s.replace(*'L0').replace(*'R1'),2)]=j[0],time
    else:
        start_pos=1
        start_time=-1
        start_color=-1
        for i in s:
            start_pos,start_color=propagate(start_pos,start_color,i=='R')
            if start_pos in color_dict:
                tmp_color,tmp_time=color_dict[start_pos]
                if start_time<tmp_time:
                    start_time=tmp_time
                    start_color=tmp_color
        print(start_color)