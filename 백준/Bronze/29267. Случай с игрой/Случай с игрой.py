s=c=0
n,*l=open(0)
for i in l:
    if i[2]=='m':c+=int(n.split()[1])
    if i[2]=='v':s=c
    if i[2]=='o':c-=1
    if i[2]=='a':c=s
    print(c)