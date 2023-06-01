a,b,c=map(int,input().split())
t=min(a//2,b)
if a+b-3*t<c:
    t-=((c+3*t-a-b)+2)//3
print(t)