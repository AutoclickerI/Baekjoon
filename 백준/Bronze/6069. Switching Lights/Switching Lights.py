[n,m],*z=[map(int,i.split())for i in open(0)]
v=0
for q,s,e in z:q and print((2**e-2**~-s&v).bit_count());v^=(2**e-2**~-s)*(1-q)