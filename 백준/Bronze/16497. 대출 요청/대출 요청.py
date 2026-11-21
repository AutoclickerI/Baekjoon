l=[0]*31
_,*s,n=open(0)
I=int
for i in s:
 for j in range(I(i[:2]),I(i[2:])):l[j]+=1
print(+(max(l)<=I(n)))