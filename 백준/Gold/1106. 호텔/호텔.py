l=[0]+[1e9]*1100
[C,_],*z=[map(int,i.split())for i in open(0)]
for c,v in z:
 for i in range(1100):l[i]=min(l[i-v]+c,l[i])
print(min(l[C:]))