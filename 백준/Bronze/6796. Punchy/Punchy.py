A=B=0
while(s:=input())<'7':
    P=s.split()
    C,X=int(P[0]),P[1]
    if C==1:exec(f'{X}={P[2]}')
    elif C == 2:eval(f'print({X})')
    else:exec(f"{X}=int(eval('+*-/'[C-3].join(P[1:]))+(C==6)*(eval('*'.join(P[1:]))<0))")