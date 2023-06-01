from bisect import*
n,*l=map(int,open(0).read().split())
d=[m:=0]
c=[-2e+9]
for i in l:
 if c[-1]<i:d+=[m:=len(c)];c+=[i]
 else:d+=[L:=bisect_left(c,i)];c[L]=i
print(m)
a=[]
while n:
 if d[n]==m:a+=[l[n-1]];m-=1
 n-=1
print(*a[::-1])