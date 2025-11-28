N,_,*l=map(int,open(0).read().split())
print(max(l[0],*[j-i+1>>1for i,j in zip(l,l[1:])],N-l[-1]))