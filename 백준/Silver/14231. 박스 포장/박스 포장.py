from bisect import*
n,*l=map(int,open(0).read().split())
d=[m:=0]
c=[-2e+9]
for i in range(n):
 if c[-1]<l[i]:d+=[m:=len(c)];c+=[l[i]]
 else:d+=[L:=bisect_left(c,l[i])];c[L]=l[i]
print(m)