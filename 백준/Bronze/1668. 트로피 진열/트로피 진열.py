_,*l=map(int,open(0))
m=c=0
for i in l:
    c+=m<(m:=max(m,i))
print(c)
m=c=0
for i in l[::-1]:
    c+=m<(m:=max(m,i))
print(c)