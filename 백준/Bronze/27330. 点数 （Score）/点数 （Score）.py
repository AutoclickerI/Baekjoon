p,q,r,s=open(0)
a=0
for i in q.split():a+=int(i);a*=1-(str(a)in s.split())
print(a)