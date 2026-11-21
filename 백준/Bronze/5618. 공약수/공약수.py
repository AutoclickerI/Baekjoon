import math
g=math.gcd(*map(int,[*open(i:=0)][1].split()))
while i<g:i+=1;g%i<1!=print(i)