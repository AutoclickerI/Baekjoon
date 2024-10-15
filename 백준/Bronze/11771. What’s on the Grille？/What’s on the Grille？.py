n=int(input())
r=range
J=''.join
m=eval('n*[0],'*n)
g=eval("[i=='.'for i in input()],"*n)
s=iter(input())
try:
    for i in r(4):
        for i,j in((i,j)for i in r(n)for j in r(n)):
            if g[i][j]:m[i][j]=x if m[i][j]else next(s)
        g=[i[::-1]for i in zip(*g)]
    print(J(map(J,m)))
except:print('invalid grille')