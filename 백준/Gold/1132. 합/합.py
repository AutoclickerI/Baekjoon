_,*s=open(0).read().split()
v=[0]*10
n0=set()
for i in s:
    for j,c in enumerate(i[::-1]):
        v[ord(c)-65]+=10**j
    n0.add(c)
sa=sorted('ABCDEFGHIJ',key=lambda i:v[ord(i)-65])
for i in sa:
    if i not in n0:
        del v[ord(i)-65]
        break
v.sort()
print(sum(-~i*j for i,j in enumerate(v)))