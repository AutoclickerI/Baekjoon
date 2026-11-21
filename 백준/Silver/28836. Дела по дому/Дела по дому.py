*q,c,x,y,z=map(int,input().split())
a,b=sorted(q)
b=min(b,a+c)
print(b/x+min(a/x+a/y+b/y,c/y+a/z))