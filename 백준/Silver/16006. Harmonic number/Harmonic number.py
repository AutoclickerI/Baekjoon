from fractions import*
print(*f'{sum(Fraction(1,i+1)for i in range(int(input())))}'.split('/'))