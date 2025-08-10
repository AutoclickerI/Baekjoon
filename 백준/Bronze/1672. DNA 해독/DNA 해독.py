f='AGCT'.find
n=int(input())-1
*s,r=input()
while s:r='ACAGCGTAATCGGAGT'[f(s.pop())*4+f(r)]
print(r)