p,q=open(a:=0)
for i in map(int,q.split()):a^=i
print(['cubelover','koosaga'][a!=0])