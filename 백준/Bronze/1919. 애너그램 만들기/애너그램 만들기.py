a,b=open(0)
print(sum(abs(a.count(i)-b.count(i))for i in{*a+b}))