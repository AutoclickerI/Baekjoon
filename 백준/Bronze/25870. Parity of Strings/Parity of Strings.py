d={}
for i in input():d[i]=d.get(i,0)^1
l=d.values()
if all(l):print(1)
elif any(l):print(2)
else:print(0)