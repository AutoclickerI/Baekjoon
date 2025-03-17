_,a,b=open(0)
print(sum(max(0,b.count(i)-a.count(i))for i in{*b}))