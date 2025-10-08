import sys
sys.setrecursionlimit(2*10**5)
input=sys.stdin.readline

def find(s):
    if d[s]!=s:
        p=find(d[s])
        c[p]+=c[s]
        c[s]=0
        d[s]=p
    return d[s]

for _ in[0]*int(input()):
    d={}
    c={}
    for _ in[0]*int(input()):
        l=input().split()
        for i in l:
            if i not in d:
                d[i]=i
                c[i]=1
        a,b=sorted(map(find,l))
        if a!=b:
            d[b]=a
            c[a]+=c[b]
            c[b]=0
        print(c[a])