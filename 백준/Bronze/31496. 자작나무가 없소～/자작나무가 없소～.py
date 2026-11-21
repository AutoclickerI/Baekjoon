s,*l=open(n:=0)
p,q=s.split()
for i in l:
    a,b=i.split()
    if q in a.split('_'):n+=int(b)
print(n)