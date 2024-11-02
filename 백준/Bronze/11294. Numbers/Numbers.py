def to_d(n,b):
    s=[]
    while n:
        s+='0123456789ABCDEFGHIJ'[n%b]
        n//=b
    return''.join(s)[::-1]
while'#'<(s:=input()):
    b=int(input())
    print(s,n:=int(input()),to_d(n,b),sep=', ')