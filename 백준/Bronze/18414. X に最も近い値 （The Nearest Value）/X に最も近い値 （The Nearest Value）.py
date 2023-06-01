a,b,c=map(int,input().split())
if min(a,b)<=c<=max(a,b):print(c)
else:print(b if abs(c-b)<abs(c-a)else a)