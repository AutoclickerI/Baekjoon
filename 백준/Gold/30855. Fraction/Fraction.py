from fractions import*
try:
    stack=[]
    for i in[*open(0)][1].split():
        if i=='(':
            stack+=i
        elif i==')':
            l=[stack.pop(),stack.pop(),stack.pop()]
            for i in range(3):
                if isinstance(l[i],int):
                    l[i]=Fraction(l[i],1)
            c,b,a=l
            assert stack.pop()=='('
            stack+=Fraction(a.numerator*c.numerator*b.denominator+a.denominator*b.numerator*c.denominator,a.denominator*c.numerator*b.denominator),
        else:
            assert i.isdigit()
            stack+=int(i),
    assert len(stack)==1 and isinstance(stack[0],Fraction)
    print(stack[0].numerator,stack[0].denominator)
except:
    print(-1)