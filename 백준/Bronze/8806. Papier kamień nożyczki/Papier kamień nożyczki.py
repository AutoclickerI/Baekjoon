_,*l=map(eval,open(0).read().split())
while l:a,b,c,d,e,f,*l=l;p=a*e+b*f+c*d-b*d-c*e-f*a;print(['GAODSAIMA'[0<p::2],'='][p==0])