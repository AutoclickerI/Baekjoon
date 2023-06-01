a=[*map(int,input().split())]
d=a[1]-a[0]
c=int(d**0.5)
print(max(2*c-1,0) if d==c**2 else 2*c if d<=c*(c+1)else 2*c+1)