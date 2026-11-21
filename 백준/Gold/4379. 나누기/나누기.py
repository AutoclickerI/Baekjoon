import math
while 1:
 try:
  a,b,c=map(int,input().split());s=f'({a}^{b}-1)/({a}^{c}-1)';m=b%c
  if m==0 and a!=1:
   if round((b-c)*math.log10(a),10)<100:
    for i in range(b//c):m+=a**(c*i)
    if len(str(m))<100:print(s,m);continue
  print(s,'is not an integer with less than 100 digits.')
 except:break