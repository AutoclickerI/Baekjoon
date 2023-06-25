_,*l=map(int,open(0))
l.sort()
m=l[0]
M=l[-1]-l[0]
import math
for i in l[1:]:
    M=math.gcd(M,i-m)
print((l[-1]-l[0])//M-len(l)+1)