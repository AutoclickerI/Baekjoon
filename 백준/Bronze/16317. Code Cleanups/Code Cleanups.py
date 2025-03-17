*a,=map(int,[*open(0)][1].split())
c,*b=1,
for x in a:f=sum(x-i for i in b)>19;b*=f^1;c+=f;b+=x,
print(c)