a,b,c,d,e,f,g,h=open(0)
for i in{*(b+d).split()}-{*f.split()}:h=h.replace(i,' ')
print(*h.split())