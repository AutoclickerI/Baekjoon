from bisect import*
l=[]
n=int(input())
for i in[0]*n:
    l+=[[*map(int,input().split())]]
l.sort()
d=[m:=0]
c=[-2e+9]
for i in range(n):
 if c[-1]<l[i][1]:d+=[m:=len(c)];c+=[l[i][1]]
 else:d+=[L:=bisect_left(c,l[i][1])];c[L]=l[i][1]
print(n-m)
a=[]
while n:
 if d[n]==m:m-=1
 else:a+=[l[n-1][0]]
 n-=1
print(*a[::-1],sep='\n')