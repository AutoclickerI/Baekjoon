n,m,*l=map(int,open(0).read().split())
l.sort()
i=j=0
d=[]
while i<n>j:d+=[t:=l[j]-l[i]]*(f:=m<=t);i+=f;j+=1-f
print(min(d))