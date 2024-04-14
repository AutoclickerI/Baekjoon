f=lambda l,r:0if r==l else(r==l+1)*l*r or f(l,l+(d:=r-l>>1))+f(l-~d,r)
print(f(1,int(input())))