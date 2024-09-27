n,w,*l=map(int,open(0).read().split())
c=v=0
for i in l:
 if v+i<w:v+=i
 else:c+=1;v=0
print(c)