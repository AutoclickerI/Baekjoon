N,*l=open(c:=0)
for i in l:p,q,r,s=i.split();c+=p[:2]!=r[:2]
print(2*int(N)/c)