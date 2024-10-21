n,*l=map(int,open(0).read().split())
print(max((str(z:=l[i]*j)in'123456789')*z or-1for i in range(n)for j in l[i+1:]))