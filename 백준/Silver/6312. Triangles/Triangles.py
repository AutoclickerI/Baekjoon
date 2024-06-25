def up(y,x,p=0):
    if y>=0<=x-p<=x+p<len(b[y]):
        if all('#'<b[y][i]for i in range(x-p,x+p+1)):
            return 2*p+1+up(y-1,x,p+1)
    return 0
def down(y,x,p=0):
    if y<n and 0<=x-p<=x+p<len(b[y]):
        if all('#'<b[y][i]for i in range(x-p,x+p+1)):
            return 2*p+1+down(y+1,x,p+1)
    return 0
v=0
while n:=int(input()):
    v+=1
    b=eval('input(),'*n)
    m=0
    for i in range(n):
        for j in range(2*n+1):
            if i+j&1:
                m=max(m,down(i,j))
            else:
                m=max(up(i,j),m)
    print(f'Triangle #{v}\nThe largest triangle area is {m}.\n')