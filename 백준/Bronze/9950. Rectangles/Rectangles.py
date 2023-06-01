*l,_,_,_=map(int,open(0).read().split())
while l:
 a,b,c,*l=l
 if a<1:a=c//b
 if b<1:b=c//a
 print(a,b,a*b)