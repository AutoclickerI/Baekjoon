n,*l=map(int,open(0).read().split())
a,b=0,sum(l)
print(min(abs((a:=a+i)-(b:=b-i))for i in l[:-1]))