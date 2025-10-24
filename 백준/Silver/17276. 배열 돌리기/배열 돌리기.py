for T in[0]*int(input()):
    n,d=map(int,input().split())
    b=[[*map(int,input().split())]for _ in[0]*n]
    r=-d%360//45
    l=[[*b[n//2]],[b[i][i]for i in range(n)],[b[i][n//2]for i in range(n)],[b[i][~i]for i in range(n)]]
    l+=[i[::-1]for i in l]
    l*=2
    p,q,r,s,*_=l[r:]
    b[n//2]=p
    for i in range(n):
        b[i][i]=q[i]
    for i in range(n):
        b[i][n//2]=r[i]
    for i in range(n):
        b[i][~i]=s[i]
    for i in b:print(*i)