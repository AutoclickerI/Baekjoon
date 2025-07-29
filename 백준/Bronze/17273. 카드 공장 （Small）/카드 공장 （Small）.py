_,_,v,w,*l=map(int,open(0).read().split())
for i in l:
 if v<=i:v,w=w,v
print(v)