from datetime import*
x,n=map(int,input().split())
d,m,g=map(int,input().split())
d=datetime(g,m,d)+timedelta(days=(x-1)*2*n+n-1)
print(d.day,d.month,d.year)