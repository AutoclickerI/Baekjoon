f=lambda p,q:sum(a+b in'PRSP'for a,b in zip(p,q))
while'E'<(s:=input()):t=input();print(f'P1: {f(s,t)}\nP2: {f(t,s)}')