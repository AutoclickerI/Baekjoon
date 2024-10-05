from collections import Counter
n,k,*l=map(int,open(a:=0).read().split())
c=Counter(l)
for i in sorted(c,reverse=True):
    a+=c[i]
    k-=c[i]
    if k<=0:
        break
print(a)