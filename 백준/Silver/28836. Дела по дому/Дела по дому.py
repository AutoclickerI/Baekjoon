*q,c,u0,u1,u2=map(int,input().split())
a,b=sorted(q)
print(min(x/u0+y/u1+z/u2 for x,y,z in[(a+min(b,a+c),a+min(b,a+c),0),(b,c,a),(a+c,c,a)]))