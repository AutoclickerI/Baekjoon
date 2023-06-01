from bisect import*
n=int(input())
l=[int(input())for i in[0]*n]
c=[0]
for i in range(n):
 if c[-1]<l[i]:m=len(c);c+=[l[i]]
 else:L=bisect_left(c,l[i]);c[L]=l[i]
print(n-m)