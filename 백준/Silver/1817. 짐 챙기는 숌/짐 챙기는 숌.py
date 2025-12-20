N,M,*l=map(int,open(w:=0).read().split())
print(sum(N>0<i==(w:=i+w*(w+i<=M))for i in l))