def p(s):
    f=0
    for i in range(len(s)-1):
        z=s[i]in'aeiou'
        f|=z
        if~-z*f:
            return s[:i]
a,b=map(p,open(0))
print(a and b and a+b or'no such exercise')