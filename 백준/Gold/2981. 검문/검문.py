import math
n=int(input())
l=sorted(int(input())for i in[0]*n)
l=[l[i+1]-l[i]for i in range(n-1)]
G=l[0]
for i in l:G=math.gcd(G,i)
print(*[i for i in range(2,G+1)if G%i==0])