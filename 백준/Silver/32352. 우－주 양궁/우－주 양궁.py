a,b,c,d,e,f,g,h,i,j,k,l=map(int,open(0).read().split())
f=lambda*l:(*sorted(l),)in[l,(2*l)[2:6]]
print(-(f(a,b,g,h)|f(c,d,i,j)or~e+l))