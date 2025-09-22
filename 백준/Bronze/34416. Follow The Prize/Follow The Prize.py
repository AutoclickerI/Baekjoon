_,p,_,*q=open(0)
p={p[:-1]}
for i in q:v={*i.split()};p=p-v or v-p
print(*p)