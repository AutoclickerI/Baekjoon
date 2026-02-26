def evaluate(v,arr):
    stack=[v]
    for i,*c in arr:
        if i=='NUM':
            stack+=int(*c),
        if i=='POP':
            stack.pop()
        if i=='INV':
            stack[-1]*=-1
        if i=='DUP':
            stack+=stack[-1],
        if i=='SWP':
            stack[-2:]=stack[-1],stack[-2]
        if i=='ADD':
            stack+=stack.pop()+stack.pop(),
        if i=='SUB':
            stack+=-(stack.pop()-stack.pop()),
        if i=='MUL':
            stack+=stack.pop()*stack.pop(),
        if i=='DIV':
            m=stack.pop()
            d=stack.pop()
            stack+=abs(d)//abs(m)*(-(m*d<0)|1),
        if i=='MOD':
            m=stack.pop()
            d=stack.pop()
            stack+=abs(d)%abs(m)*(-(d<0)|1),
        if stack:
            assert-10**9<=stack[-1]<=10**9
    assert len(stack)==1
    return stack[-1]
while'QUIT'!=(s:=input()):
    arr=[s.split()]
    while s!='END'!=(s:=input()):
        arr+=s.split(),
    for _ in[0]*int(input()):
        try:
            print(evaluate(int(input()),arr))
        except:
            print('ERROR')
    input()
    print()