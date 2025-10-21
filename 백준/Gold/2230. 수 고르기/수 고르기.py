n,m,*l=map(int,open(0).read().split())
l.sort()
i=j=0
d=11**9
while i<n>j:
 if(t:=l[j]-l[i])<m:j+=1
 else:d=min(d,t);i+=1
print(d)