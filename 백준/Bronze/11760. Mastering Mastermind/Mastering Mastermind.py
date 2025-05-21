a,b,c=input().split()
print(s:=sum(map(str.__eq__,b,c)),sum(min(b.count(i),c.count(i))for i in{*b})-s)