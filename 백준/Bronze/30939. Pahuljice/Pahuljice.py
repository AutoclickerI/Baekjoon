n,m=map(int,input().split())
s=eval('input(),'*n)
travel=lambda y,x,dy,dx,d,t:travel(y+dy,x+dx,dy,dx,d+1,t)if 0<=y<n and 0<=x<m and s[y][x]==t else d
print(max(0,*[min(travel(y+dy,x+dx,dy,dx,0,t)for dy,dx,t in zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1],'\|/--/|\\'))for y in range(n)for x in range(m)if s[y][x]=='+']))