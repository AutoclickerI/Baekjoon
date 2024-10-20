for T in range(int(input())):
    v=int(input())
    m,*l=map(int,input().split())
    s=e=0
    a=0
    for idx,i in enumerate(l):
        if a<=v//m*(i-m):
            e=s,idx+1
            a=v//m*(i-m)
        if i<m:
            s=idx+1
            m=i
    if a==0:
        a='IMPOSSIBLE'
    else:
        a='%d %d %d'%(e[0]+1,e[1]+1,a)
    print(f'Case #{T+1}:',a)