import math
while 1:
 try:
  a,b,c=map(int,input().split())
  s=f'({a}^{b}-1)/({a}^{c}-1)'
  if b%c==0 and a!=1:
   if round((b-c)*math.log10(a),10)<100:
    p=b//c;sum=0
    for i in range(p):sum+=a**(c*i)
    if len(str(sum))<100:print(s,sum);continue
  print(s,'is not an integer with less than 100 digits.')
 except:break