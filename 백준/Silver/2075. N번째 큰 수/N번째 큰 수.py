I=lambda:map(int,input().split())
[N],*l=I(),
exec('l=sorted(l+[*I()])[-N:];'*N)
print(l[0])