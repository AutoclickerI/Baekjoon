D1,D2=map(int,input().split())
r=0
v=[2000*[0]for _ in range(2001)]
import math
for i in range(D1,D2+1):
    for j in range(i):
        gcd=math.gcd(j,i)
        p,q=i//gcd,j//gcd
        if v[p][q]<1:
            r+=1
            v[p][q]=1
print(r)