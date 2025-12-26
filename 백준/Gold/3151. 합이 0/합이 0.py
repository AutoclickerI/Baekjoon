n,*l=map(int,open(0).read().split())
l.sort()
r=0
import math
for i in range(n):
    s=i+1
    e=n-1
    while s<e:
        if l[s]+l[e]+l[i]==0:
            if l[s]==l[e]:
                r+=math.comb(e-s+1,2)
                break
            else:
                le=1
                ri=1
                while l[s]==l[s+1]:
                    s+=1
                    le+=1
                while l[e]==l[e-1]:
                    e-=1
                    ri+=1
                r+=le*ri
        if l[s]+l[e]+l[i]<0:
            s+=1
        else:
            e-=1
print(r)