p=65;t=0
for c in input():t+=min(x:=abs(p-(p:=ord(c))),26-x)
print(t)