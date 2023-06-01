R=range(n:=int(input()))
s=sum(l:=[*map(int,input().split())])
a=0
for i in R:
 v=0
 for j in R:v+=l[i+j-n];a-=min(0,v)//s
print(a)