from collections import deque
for _ in[0]*int(input()):
    n=int(input())
    *t,=map(int,input().split())
    s=set()
    for i in range(n):
        for j in range(i+1,n):
            s|={(t[i],t[j])}
    for _ in[0]*int(input()):
        a,b=map(int,input().split())
        if(b,a)not in s:
            a,b=b,a
        s-={(b,a)}
        s|={(a,b)}
    flag=1
    count=0
    edges=[[]for _ in[0]*-~n]
    dag=[0]*-~n
    for a,b in s:
        edges[a]+=b,
        dag[b]+=1
    dq=deque()
    for i in range(1,n+1):
        if dag[i]<1:dq+=i,
    ans=[]
    while dq:
        if 1<len(dq):
            flag=0
        n=dq.popleft()
        ans+=n,
        for e in edges[n]:
            dag[e]-=1
            if dag[e]<1:
                dq+=e,
    if sum(dag):
        print('IMPOSSIBLE')
    elif flag:
        print(*ans)
    else:
        print('?')