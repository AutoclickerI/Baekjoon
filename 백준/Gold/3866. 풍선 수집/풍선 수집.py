import sys
input=sys.stdin.readline

while n:=int(input()):
    l=[[*map(int,input().split())]for _ in[0]*n]
    l.sort(key=lambda i:i[1])
    mc=[float('inf')]*4
    pp=0
    pt=0
    mc[0]=0
    l+=[0,float('inf')],
    cnt=0
    for p,t in l:
        cnt+=1
        nmc=[float('inf')]*4
        for i in range(4):
            nt=pt+pp*-~i+p
            if nt<=t:
                nmc[1]=min(nmc[1],mc[i]+pp+p)
        for i in range(3):
            nt=pt+abs(pp-p)*-~i
            if nt<=t:
                nmc[i+1]=min(nmc[i+1],mc[i]+abs(pp-p))
        mc=nmc
        pp=p
        pt=t
        mv=min(mc)
        if mv==float('inf'):
            print('NG',cnt)
            break
    else:
        print('OK',mc[1])