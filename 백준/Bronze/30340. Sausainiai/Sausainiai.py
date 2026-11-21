x,*c=0,
for i in[*open(0)][1:]:a,b=map(int,i.split());c+=a+b,;x-=b
print(x+sum(sorted(c)[::-2]))