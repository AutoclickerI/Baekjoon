import math
*S,=input()
try:
 for i in input():S.remove(i)
 a=sum(-~k*math.perm(len(S),k)for k in range(1+len(S)))
except:a=0
print(a)