*l,r=[eval(i.replace(' ','+1j*'))for i in open(0)]
a,b,c=[abs(l[i]-l[j])for i,j in((0,1),(0,2),(1,2))]
print(((4*(a*b)**2-(a*a+b*b-c*c)**2)**.5/(a+b+c)/2/r-1)*100)