import sys
input=sys.stdin.readline

from heapq import*

def precendence(s):
    global cnt,pre
    if s in d:
        return d[s]
    pre+=s,
    d[s]=cnt
    cnt+=1
    return d[s]
    

while 1:
    N,M=map(int,input().split())
    if N==M==0:
        break
    d={}
    cnt=0
    
    edges={}
    deg={}
    
    pre=[]
    
    for _ in[0]*N:
        p1,_,*q=input().split()
        precendence(p1)
        deg[p1]=len(q)
        for i in q:
            precendence(i)
            edges[i]=edges.get(i,[])
            edges[i]+=p1,
    
    c={}
    hq=[]
    stay=[]
    for i in pre:
        if deg.get(i,0)<1:
            heappush(hq,(precendence(i),i,-1))
            c[i]=1
    
    ans=[[]]
    
    while hq or stay:
        if M<=len(ans[-1]):
            ans+=[],
        while stay and stay[0][0]<=len(ans):
            prev,prec,n=heappop(stay)
            heappush(hq,(prec,n,prev))
        if hq:
            prec,n,prev=heappop(hq)
            ans[-1]+=n,
            for e in edges.get(n,[]):
                deg[e]-=1
                if deg[e]<1:
                    heappush(stay,(len(ans)+1,precendence(e),e))
        else:
            ans+=[],
    print('Formatura em',len(ans),'semestres')
    for i in range(len(ans)):
        print('Semestre',i+1,':',*sorted(ans[i]))