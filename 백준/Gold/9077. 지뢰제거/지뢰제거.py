import sys
input=sys.stdin.readline
for T in range(int(input())):
    d={}
    m=0
    for _ in[0]*int(input()):
        x,y=map(int,input().split())
        for i in range(-5,6):
            for j in range(-5,6):
                d[(x+i)*20000+y+j]=d.get((x+i)*20000+y+j,0)+1
                m=max(m,d[(x+i)*20000+y+j])
    print(m)