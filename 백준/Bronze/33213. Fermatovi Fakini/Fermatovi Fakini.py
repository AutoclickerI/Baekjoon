n,*l=map(int,open(0).read().split())
o=sum(i%2for i in l)
v=2-(o*2>n)
while v in l:v+=2
print(v)