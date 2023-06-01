i,*l=open(0)
p,q,r=map(int,i.split())
for i in l:print('RKEEMEOPV E'[q in map(int,i.split()[1:])::2])