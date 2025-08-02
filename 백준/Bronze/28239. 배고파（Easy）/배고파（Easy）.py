f=int.bit_length
for i in[*open(0)][1:]:m=int(i);y=f(m-1)-1;print(f(m-2**y)-1,y)