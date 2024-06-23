input()
s=input()
p={(0,0)}
l=set()
x=y=0
for i in s:
    px,py=x,y
    if i=='N':
        y+=1
    if i=='E':
        x+=1
    if i=='W':
        x-=1
    if i=='S':
        y-=1
    p|={(x,y)}
    l|={tuple(sum(sorted([[x,y],[px,py]]),[]))}
print(1-len(p)+len(l))