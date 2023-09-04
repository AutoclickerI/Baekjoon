a,b=open(0)
*l,=a
for i in range(len(l)):
    if l[i] in b:l[i]=l[i].lower()
print(''.join(l))