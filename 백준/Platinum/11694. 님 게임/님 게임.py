p,q=open(0)
a=f=0
for i in map(int,q.split()):a^=i;f|=a
print(['cubelover','koosaga'][(a!=0)-(f==1)])