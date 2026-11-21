m=e=0
for i in[*open(0)][1:]:p,q=map(int,i.split());m=max(m,p-e);e=p*q or e
print(m)