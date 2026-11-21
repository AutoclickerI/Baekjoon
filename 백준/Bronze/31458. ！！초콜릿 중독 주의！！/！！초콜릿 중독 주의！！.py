for _ in[0]*int(input()):
    s=input()
    n='0'if'0'in s else'1'
    i=s.index(n)
    if i!=len(s)-1:
        n='1'
    print(i%2^int(n))