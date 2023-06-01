n,*l=map(int,open(0).read().split())
R=range(n)
s=sum(l)
a=0
for i in R:
 v=0
 for j in R:v+=l[i+j-n];a-=v*(v<0)//s
print(a)