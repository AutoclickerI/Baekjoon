a=list(map(int,input().split(':')))
a=a[0]*3600+a[1]*60+a[2]
b=list(map(int,input().split(':')))
b=b[0]*3600+b[1]*60+b[2]
print(b-a if b-a>=0 else b-a+3600*24)