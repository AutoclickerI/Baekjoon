m=0
for i in[*open(0)][1:]:p,q,r=map(int,i.split());q+=r;m=max(m,p*q*(1+(p==q)))
print(m)