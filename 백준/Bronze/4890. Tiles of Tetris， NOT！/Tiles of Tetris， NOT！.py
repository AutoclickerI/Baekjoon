import math
for i in[*open(0)][:-1]:w,h=map(int,i.split());g=math.gcd(w,h);print(w//g*(h//g))