v=[2000*[r:=0]for _ in range(2001)]
import math
for i in range(*eval(input().replace(' ',',1+'))):
 for j in range(i):g=math.gcd(j,i);r+=v[p:=i//g][q:=j//g]<1;v[p][q]=1
print(r)