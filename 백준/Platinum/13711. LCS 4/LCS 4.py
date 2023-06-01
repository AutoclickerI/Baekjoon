from bisect import*
n=int(input())
l1=[*map(int,input().split())]
l2=[*map(int,input().split())]
l=[[l1[i],l2.index(l1[i])]for i in range(n)]
d=[m:=0]
c=[-2e+9]
for i in range(n):
 if c[-1]<l[i][1]:d+=[m:=len(c)];c+=[l[i][1]]
 else:d+=[L:=bisect_left(c,l[i][1])];c[L]=l[i][1]
print(m)