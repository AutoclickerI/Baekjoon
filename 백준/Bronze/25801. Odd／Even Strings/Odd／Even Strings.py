s=input()
l=[]
for i in s:l+=[s.count(i)%2]
if all(l):print(1)
elif any(l):print('0/1')
else:print(0)