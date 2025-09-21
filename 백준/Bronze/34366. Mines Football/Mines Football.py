_,*l=[[*map(int,i.split()[1:])]for i in open(0)]
*x,=map(sum,l)
print(max(z:=sum(l,[])),min(z),max(x),min(x))