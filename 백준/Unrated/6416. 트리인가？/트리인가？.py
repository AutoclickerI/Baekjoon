l=[*map(int,open(0).read().split())][:-2][::-1]
case=0
while l:
    case+=1
    d={}
    x={}
    while True:
        s,e=l.pop(),l.pop()
        if s==e==0:
            break
        x[e]=x[s]=1
        d[s]=d.get(s,[])
        d[s]+=e,
        d[e]=d.get(e,[])
        d[e]+=s,
    def DFS(n,prev):
        if x[n]<1:
            return False
        x[n]=0
        f=True
        for e in d[n]:
            if e!=prev:
                f=DFS(e,n) and f
        return f
    if len(d)<1:
        print('Case',case,'is a tree.')
    else:
        print('Case',case,'is','not a tree.'[(DFS([*d.keys()][0],-1)and not any(x.values()))*4:])