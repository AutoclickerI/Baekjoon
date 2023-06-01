from bisect import*
n=int(input())
l=list(map(int,input().split()))
d=[m:=0]
c=[-2e+9]
for i in range(n):
 if c[-1]<l[i]:c+=[l[i]];d+=[m:=len(c)-1]
 else:d+=[bisect_left(c,l[i])];c[d[-1]]=l[i]
print(len(l)-m)