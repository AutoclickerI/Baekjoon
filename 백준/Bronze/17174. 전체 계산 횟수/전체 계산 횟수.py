p,q=map(int,input().split())
a=p
while p:a+=(p:=p//q)
print(a)