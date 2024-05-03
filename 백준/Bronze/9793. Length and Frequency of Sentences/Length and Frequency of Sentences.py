x=eval('len(input().split()),'*int(input()))
for i in sorted({*x}):print(i,x.count(i))