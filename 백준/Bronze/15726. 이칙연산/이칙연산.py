a,b,c=map(int,input().split())
if b==c:
    print(a)
else:
    print(a*max(b,c)//min(b,c))