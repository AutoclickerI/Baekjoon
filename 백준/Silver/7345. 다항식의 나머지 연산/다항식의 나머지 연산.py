for _ in[0]*int(input()):
    n=int(''.join(input().split()[1:]),2)
    v=0
    c,*l=map(int,input().split())
    while c:
        v^=n*l[-c]<<c-1
        c-=1
    d=int(''.join(input().split()[1:]),2)
    while d.bit_length()<=v.bit_length():
        v^=d<<v.bit_length()-d.bit_length()
    print(v.bit_length(),*f'{v:b}')