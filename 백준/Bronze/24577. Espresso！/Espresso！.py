s,*l=[eval(i.split()[-1].replace('L','+1'))for i in open(0)]
v=s
c=0
for i in l:
    v-=i
    if v<0:v=s-i;c+=1
print(c)