_,*l,m=open(c:=0)
s=''
for i in l:f=all(i in('*',j)for i,j in zip(m,i+'_'*99));c+=f;s+=i*f
print(c,s)