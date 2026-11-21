N,C,S,*l=map(int,open(p:=0).read().split())
a=1==S
for i in l:p+=i;a+=p%N==~-S
print(a)