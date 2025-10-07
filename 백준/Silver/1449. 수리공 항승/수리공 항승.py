_,L,*l=map(int,open(c:=0).read().split())
v=-L
for i in sorted(l):
 if v+L<=i:c+=1;v=i
print(c)