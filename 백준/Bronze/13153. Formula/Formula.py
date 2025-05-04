l,m,n,r=[eval(i.replace(' ','+1j*'))for i in open(0)]
a,b,c=map(abs,[l-m,l-n,m-n])
print(((4*a*a*b*b-(a*a+b*b-c*c)**2)**.5/(a+b+c)/2/r-1)*100)