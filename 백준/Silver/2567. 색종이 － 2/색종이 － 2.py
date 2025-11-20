s=set()
for i in[*open(0)][1:]:
    y,x=map(int,i.split())
    s|={(y+j,x+k)for j in range(10)for k in range(10)}
a=0
for y,x in s:
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        if(y+dy,x+dx)not in s:a+=1
print(a)