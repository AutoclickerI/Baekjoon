s=[0]*1001
_,*a=[[*map(int,i.split())]for i in open(0)]
for v in a:
 for k in range(*v):s[k]+=1
print(1001-min(s[i:j].count(1)for i,j in a)-s.count(0))