A=input()
B=input()

v=[[0]*-~len(A)]

for i in range(len(B)):
    t=[0]
    for j in range(len(A)):
        t+=max(t[-1],v[-1][j+1],v[-1][j]+(A[j]==B[i])),
    v+=t,

y=len(B)
x=len(A)
a=''
while v[y][x]:
    while v[y-1][x]==v[y][x]:
        y-=1
    while v[y][x-1]==v[y][x]:
        x-=1
    a+=A[x-1]
    x-=1

print(len(a))