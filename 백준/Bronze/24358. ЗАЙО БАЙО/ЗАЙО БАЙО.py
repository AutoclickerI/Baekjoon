from datetime import*
x,n,d,m,g=map(int,open(0).read().split())
d=datetime(g,m,d)+timedelta(days=~-x*2*n+n-1)
print(d.day,d.month,d.year)