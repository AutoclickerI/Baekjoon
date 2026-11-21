n,s,*a=open(0).read().split()
x=a[::2].index(s)*2
print(a[1:x:2].count(a[x+1]))