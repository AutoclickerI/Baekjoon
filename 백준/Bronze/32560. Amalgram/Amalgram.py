a,b=open(0)
for i in{*a,*b}-{'\n'}:print(end=i*max(a.count(i),b.count(i)))