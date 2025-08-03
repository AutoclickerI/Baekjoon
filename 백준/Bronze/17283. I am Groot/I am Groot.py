L,R=map(int,open(0))
a=i=0
while(L:=L*R//100)>5:i+=1;a+=L<<i
print(a)