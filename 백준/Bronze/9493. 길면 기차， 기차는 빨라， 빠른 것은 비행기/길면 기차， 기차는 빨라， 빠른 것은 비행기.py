from decimal import*
getcontext().prec=999
while'1'<(s:=input()):
    p,q,r=map(int,s.split())
    t=round(abs(p*3600/q-p*3600/r))
    print(f'{t//3600}:{t//60%60:02}:{t%60:02}')