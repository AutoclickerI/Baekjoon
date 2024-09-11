from fractions import*
a=sum(Fraction(1,i+1)for i in range(int(input())))
print(a.numerator,a.denominator)