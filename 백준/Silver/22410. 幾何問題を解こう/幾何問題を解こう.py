import math
p,q=map(int,input().split())
q//=math.gcd(p,q)
d={}
for i in range(2,int(q**.5)+1):
    while q%i<1:
        q//=i
        d[i]=d.get(i,0)+1
d[q]=1
mv=max(d.values())
a=1
for i in d:a*=i
print(a)