p=65
print(sum(min(x:=abs(p-(p:=ord(c))),26-x)for c in input()))