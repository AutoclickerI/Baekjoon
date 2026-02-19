s=input()
l=set()
*p,=range(len(s))
while p:
    mv=max([i for i in p if i in l]or[-1])
    nv=min(range(mv+1,p[-1]+1),key=lambda i:s[i])
    l.add(nv)
    print(*[s[i]for i in sorted(l)],sep='')
    while p and p[-1]in l:p.pop()