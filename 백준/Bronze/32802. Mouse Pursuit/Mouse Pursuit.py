_,*l,n=open(0)
C=G=0
GHT=1
S=-1
for i in l:p,s,c,g=map(eval,i[3:].split());f=p*(s<int(n));C+=c*f;G+=g*f
print(C,G)