from fractions import Fraction
c1,c2,c3,c4,c5,c6=map(int,input().split()) 
x1,x3=map(int,str(Fraction(c1,c5)).split('/'))
x5,x7=map(int,str(Fraction(c6,c3)).split('/'))
x2=c5//x3
x6=c6//x5
print(x1,x2,x3,x5,x6,x7)