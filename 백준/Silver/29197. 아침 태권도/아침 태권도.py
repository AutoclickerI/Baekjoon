import math
s={}
for i in[*open(0)][1:]:p,q=map(int,i.split());g=math.gcd(p,q);s[p//g,q//g]=0
print(len(s))