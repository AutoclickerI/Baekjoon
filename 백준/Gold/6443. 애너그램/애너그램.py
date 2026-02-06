from itertools import*

def DFS(i,ss):
    if i==len(d):
        r.add(''.join(a))
        return
    for v in combinations(ss,d[p[i]]):
        for j in v:
            a[j]=p[i]
        DFS(i+1,ss-{*v})
for _ in[0]*int(input()):
    s=input()
    d={}
    for i in s:d[i]=d.get(i,0)+1
    p=[*d]
    r=set()
    a=[0]*len(s)
    pos={*range(len(s))}
    DFS(0,pos)
    for i in sorted(r):
        print(i)