A=B=f=0
a='D'
for i,j in zip(l:=open(0).read().split(),l[10:]):a=a*(i==j)or'AB'[i<j];A+=1+2*(i>j)-(i<j);B+=1+2*(i<j)-(i>j)
print(A,B,a*(A==B)or'AB'[A<B])