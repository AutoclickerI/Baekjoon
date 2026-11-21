n,z=open(0)
n=int(n)
s=n*~-n//-2
t=''
for c in z:
 t+=c
 if'0'>c:s+=int(t);t=''
print(s)