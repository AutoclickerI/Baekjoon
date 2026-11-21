[c,r],*l,_=[map(int,i.split())for i in open(0)]
x=y=0
for p,q in l:x,y=max(0,min(x+p,c)),max(0,min(y+q,r));print(x,y)