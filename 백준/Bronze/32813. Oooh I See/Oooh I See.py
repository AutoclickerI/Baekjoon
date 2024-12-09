r,c=map(int,input().split())
b=eval('input(),'*r)
a=[]
for y in range(1,r-1):
    for x in range(1,c-1):
        if b[y][x]=='0' and all(b[y+dy][x+dx]=='O'for dy in range(-1,2)for dx in range(-1,2)if dy or dx):
            a+=(y+1,x+1),
if len(a)==1:
    print(*a[0])
elif a:
    print('Oh no!',len(a),'locations')
else:
    print('Oh no!')