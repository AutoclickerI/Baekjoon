import math
n=int(input())
l=sorted(int(input())for i in[0]*n)
l=[l[i+1]-l[i]for i in range(n-1)]
G=l[0]
for i in l[1:]:G=math.gcd(G,i)
for i in range(2,G+1):
    if G%i==0:print(i,end=' ')