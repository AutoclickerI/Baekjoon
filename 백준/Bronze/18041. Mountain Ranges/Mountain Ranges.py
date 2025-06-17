n,x,*l=map(int,open(0).read().split())
print(max([s:=1]+[s:=s*(j+~i<x)+1for i,j in zip(l,l[1:])]))