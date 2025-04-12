n,s,*a=open(c:=0).read().split()
m=s=int(s)
for p,*q in a:
 if(x:=int(p)+([]<q))>m:m=s;c+=1
 m-=x
print(c)