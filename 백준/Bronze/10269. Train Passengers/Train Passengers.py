[c,n],*x=[map(int,i.split())for i in open(0)]
y=z=0
for p,q,r in x:y|=z<p;z+=q-p;y|=z>c or z<c and r
print((y+z!=0)*'im'+'possible')