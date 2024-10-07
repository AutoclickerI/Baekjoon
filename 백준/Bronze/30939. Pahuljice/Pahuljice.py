n,m=map(int,input().split())
s=eval('input(),'*n)

def travel(y,x,dy,dx,d,t):
    if 0<=y<n and 0<=x<m and s[y][x]==t:
        return travel(y+dy,x+dx,dy,dx,d+1,t)
    return d

a=0

for y in range(n):
    for x in range(m):
        v=50
        if s[y][x]=='+':
            for dy,dx,t in(-1,-1,'\\'),(-1,0,'|'),(-1,1,'/'),(0,-1,'-'),(0,1,'-'),(1,-1,'/'),(1,0,'|'),(1,1,'\\'):
                v=min(v,travel(y+dy,x+dx,dy,dx,0,t))
            a=max(v,a)
print(a)