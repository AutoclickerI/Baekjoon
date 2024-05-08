n,s=open(0)
f=n.find
print(1+sum(f(x)>=f(y)for x,y in zip(s,s[1:])))