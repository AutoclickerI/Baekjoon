from bisect import*
n=int(input())
d=[m:=0]
c=[-2e+9]
for i in map(int,input().split()):
 if c[-1]<i:c+=[i];d+=[m:=len(c)-1]
 else:d+=[bisect_left(c,i)];c[d[-1]]=i
print(m)