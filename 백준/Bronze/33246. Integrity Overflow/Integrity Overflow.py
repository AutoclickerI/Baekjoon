a,k,*l=open(b:=0);k=k[:-1]
for i in l:x,y=i.split();b|=((len(k)==len(x))&(sum(i!=j for i,j in zip(k,x))<2))^(y<'B')
print(['SYSTEM SECURE','INTEGRITY OVERFLOW'][b])