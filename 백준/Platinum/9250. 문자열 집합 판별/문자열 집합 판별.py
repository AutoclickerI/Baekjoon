N,*l=open(0)
N=int(N)

t=[[0]*26]
f=[0]
e=[0]

for w in l[:N]:
    p=0
    for c in w[:-1]:
        c=ord(c)-97
        if t[p][c]<1:
            t[p][c]=len(t)
            t+=[[0]*26]
            f+=0,
            e+=0,
        p=t[p][c]
    e[p]=1

q=[t[0][i]for i in range(26)if t[0][i]]

for x in q:
    e[x]|=e[f[x]]
    
    for i in range(26):
        y=t[x][i]
        if y:
            f[y]=t[f[x]][i]
            q+=y,
        else:
            t[x][i]=t[f[x]][i]

for w in l[N+1:]:
    p=0
    f=1
    
    for c in w[:-1]:
        p=t[p][ord(c)-97]
        
        if e[p]:
            f=0
    
    print('YNEOS'[f::2])