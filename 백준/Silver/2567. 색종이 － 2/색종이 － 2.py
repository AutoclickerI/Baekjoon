s=set()
for i in[*open(0)][1:]:y,x=map(int,i.split());s|={(y+v//10,x+v%10)for v in range(100)}
print(sum(1-((y+dy,x+dx)in s)for y,x in s for dy,dx in((-1,0),(1,0),(0,1),(0,-1))))