def to_roman(n):
    s=''
    if n<1 or 4999<n:
        return 'out of range exception'
    while n>999:
        s+='M'
        n-=1000
    if n>899:
        s+='CM'
        n-=900
    if n>499:
        s+='D'
        n-=500
    if n>399:
        s+='CD'
        n-=400
    while n>99:
        s+='C'
        n-=100
    if n>89:
        s+='XC'
        n-=90
    if n>49:
        s+='L'
        n-=50
    if n>39:
        s+='XL'
        n-=40
    while n>9:
        s+='X'
        n-=10
    if n>8:
        s+='IX'
        n-=9
    if n>4:
        s+='V'
        n-=5
    if n>3:
        s+='IV'
        n-=4
    s+='I'*n
    return s

def to_int(s):
    d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    return sum(d[i]for i in s)-2*sum(d[i]for i,j in zip(s,s[1:])if d[i]<d[j])

stack=[]
for s in open(0):
    s=s[:-1]
    if s=='+':
        if len(stack)<2:
            print('stack underflow')
        else:
            stack+=stack.pop()+stack.pop(),
    elif s=='/':
        if len(stack)<2:
            print('stack underflow')
        else:
            t=stack.pop()
            if t==0:
                print('division by zero exception')
            else:
                stack+=stack.pop()//t,
    elif s=='-':
        if len(stack)<2:
            print('stack underflow')
        else:
            t=stack.pop()
            stack+=stack.pop()-t,
    elif s=='*':
        if len(stack)<2:
            print('stack underflow')
        else:
            stack+=stack.pop()*stack.pop(),
    elif s=='=':
        if len(stack)<1:
            print('stack underflow')
        else:
            print(to_roman(stack[-1]))
    else:
        stack+=to_int(s),