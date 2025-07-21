i=0
a=[0]+[i:=i+int(j)for j in input().split()]
for i in a:
 for j in a:print(abs(j-i))