_,L,*A=map(int,open(a:=0).read().split())
B=[a:=a+i for i in[0]*L+A]
print(sum(128<b-a<139for a,b in zip(B,B[L:])))