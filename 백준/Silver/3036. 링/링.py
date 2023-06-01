from fractions import Fraction
input()
l=list(map(int,input().split()))
c=1
for k in range(len(l)-1):
    c=Fraction(c,1)*Fraction(l[k],l[k+1])
    print(f'{c}/1'if c==int(c)else c)