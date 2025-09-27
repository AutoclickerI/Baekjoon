F,S,G,U,D=map(int,input().split())
v=[1]*F
q=[(S-1,0)]
for i,c in q:
    if i+U<F and v[i+U]:
        v[i+U]=0
        q+=(i+U,c+1),
    if 0<=i-D and v[i-D]:
        v[i-D]=0
        q+=(i-D,c+1),
    if i==G-1:
        exit(print(c))
print('use the stairs')