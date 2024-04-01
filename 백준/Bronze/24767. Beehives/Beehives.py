while 1:
    s=input()
    if s=='0.0 0':break
    d,N=map(eval,s.split())
    l=[[*map(eval,input().split())]for _ in[0]*N]
    a=b=0
    res=[0]*N
    for i in range(N-1):
        for j in range(i+1,N):
            t=(l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2<d*d
            res[i]|=t
            res[j]|=t
    a=sum(res)
    print(f'{a} sour, {N-a} sweet')