n,a=open(0)
s=c=0
for x in a.split():s=abs(int(x)-s)
for y in b'd2\n':c+=s//y;s%=y
print(c)