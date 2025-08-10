f='AGCT'.find
_,(*s,r,_)=open(0)
while s:r='ACAGCGTAATCGGAGT'[f(s.pop())*4+f(r)]
print(r)