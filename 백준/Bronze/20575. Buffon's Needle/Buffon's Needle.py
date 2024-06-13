N,*l=open(c:=0)
for i in l:x,*t=i.replace(*'. ').split();c+=x!=t[3]
print(2*int(N)/c)