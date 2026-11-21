n,w,*l=map(int,open(0).read().split())
c=v=0
for i in l:v+=i;f=w<=v;c+=f;v-=f*v
print(c)