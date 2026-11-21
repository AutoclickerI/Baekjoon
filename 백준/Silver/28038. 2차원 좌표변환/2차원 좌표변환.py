from cmath import*
for _ in[0]*int(input()):
    s=input()
    p,q=map(eval,input().split())
    if s=='1':
        p,q=polar(p+1j*q)
        print(p,q%(2*pi))
    else:
        p=rect(p,q)
        print(p.real,p.imag)